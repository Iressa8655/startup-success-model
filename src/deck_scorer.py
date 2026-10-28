"""把一份 deck 的子分數變成三個支柱分數、建議和待查核清單。

用法  python deck_scorer.py example_deck_scores.json
規則說明見 RUBRIC.md
"""
import json
import sys
from pathlib import Path

RUBRIC = json.loads((Path(__file__).parent / 'rubric.json').read_text())
NEUTRAL = 3  # 中性分數，只是自稱的分數往這裡拉


def adjust_score(entry):
    """依查核狀態調整單一子分數。

    :param entry: {'score': 1-5, 'status': verified/claimed/contradicted}
    :type entry: dict
    :return: 調整後分數
    :rtype: float
    """
    if entry['status'] == 'contradicted':
        return 1.0  # 查了不符，直接最低
    if entry['status'] == 'claimed':
        discount = RUBRIC['claimed_discount']
        return entry['score'] - discount * (entry['score'] - NEUTRAL)
    return float(entry['score'])


def score_deck(deck):
    """計算支柱分數與建議。

    :param deck: 子分數字典加 red_flags 清單
    :type deck: dict
    :return: 支柱分數、建議、待人工查核項目
    :rtype: dict
    """
    pillar_scores = {}
    to_check = []
    for pillar in ['team', 'upside', 'thesis']:
        adjusted = []
        for criterion in RUBRIC[pillar]:
            entry = deck['scores'].get(criterion)
            if entry is None:
                to_check.append(criterion + ' (missing)')
                continue
            if entry['status'] == 'claimed':
                to_check.append(criterion + ' (claimed only)')
            adjusted.append(adjust_score(entry))
        pillar_scores[pillar] = round(sum(adjusted) / len(adjusted), 2)

    limits = RUBRIC['thresholds']
    if deck.get('red_flags'):
        pillar_scores['team'] = min(pillar_scores['team'], 2)  # 紅旗封頂

    if min(pillar_scores.values()) <= limits['pass_max_pillar']:
        recommendation = 'Pass'
    elif min(pillar_scores.values()) >= limits['meeting_min_pillar']:
        recommendation = 'Take Meeting'
    else:
        recommendation = 'Maybe'
    return {
        'pillars': pillar_scores,
        'recommendation': recommendation,
        'human_checks': to_check,
        'red_flags': deck.get('red_flags', []),
    }


if __name__ == '__main__':
    deck_scores = json.loads(Path(sys.argv[1]).read_text(encoding='utf-8'))
    print(json.dumps(score_deck(deck_scores), indent=2, ensure_ascii=False))
