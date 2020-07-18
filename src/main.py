#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Story: "title"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World
from storybuilder.assets import basic
from storybuilder.assets import common_rubi
from config import ASSET
# import scenes


################################################################
#
#   1. Initialize
#   2. Story memo
#   3. Structure    - 1/8: 1K * 10
#   4. Spec
#   5. Plot         - 1/4: 2.5K * 10
#   6. Scenes
#   7. Conte        - 1/2: 5K * 10
#   8. Layout
#   9. Draft        - 1/1: 10K *10
#
################################################################


# Constant
TITLE = "大賢者さまのパンツ！"
MAJOR, MINOR, MICRO = 1, 1, 0
COPY = "パンツ・イズ・ジャスティス"
ONELINE = "知らない世界でパンツに転生していた男は、そこで出会った見知らぬ女性に履かれる。そこから彼のパンツ人生が幕を開けた"
OUTLINE = "約10万字のパンツ転生ファンタジィ。知らない世界でパンツに転生した男を履いた女性は、その世界で大賢者と恐れられる女性だった。パンツや衣服の文化のない世界に、パンツ男は着衣の文化を広めていく"
THEME = "パンツは人間らしさの基本だった"
GENRE = "ファンタジィ／転生"
TARGET = "20-30台（男女）"
SIZE = "100K〜"
CONTEST_INFO = "第二回アーススター・ノベル大賞"
CAUTION = ""
NOTE = ""
SITES = ["エブリスタ", "小説家になろう", "ノベルアッププラス", "カクヨム"]
RELEASED = (7, 12, 2020)


# Episode



# Chapter
def ch_main(w: World):
    return w.chapter('main',
            "下着メーカーに勤務する彼女に振られた会社員の男性は、電車内で痴漢をしていた男を捕まえようとして飛び出してきたトラックに轢き殺される",
            "目覚めるとそこは知らない薄暗い場所",
            "見知らぬ女に話しかけられたが、その女は世界で大賢者と恐れられた存在であり、幽閉されたと告白する",
            "その強大な力によって、逆に牢獄から出られなくなっていた",
            "男であるパンツを履くことでその力を制御し、牢獄から出ることができた",
            "五百年ぶりに牢獄を出た大賢者の女は、パンツと共に全く姿を変えてしまった世界で、自分を陥れた妹たちをこらしめようと考える",
            "牢獄を出るときに、現在の大賢者と遭遇し、こてんぱんにやられてしまう",
            "目覚めると山間の村里で、助けられていた",
            "彼女もどこか別の世界の記憶を持つ住人だった",
            "男は自分以外にもこの世界に転生してきた人がいると知る",
            "彼女を仲間に入れ、三人？で旅立つ",
            "大賢者の住処へとやってきた",
            "そこで力を封じたものを手に入れる為だ",
            "しかし、そこで裏切り者の妹が待ち伏せていた",
            "妹もガーター・ベルトを手に入れていた",
            "ガーターは男が捕まえようとして死の原因となった痴漢男だった",
            "ガーターに操られる妹から何とか逃げ出す",
            "",
            )

# History

# Note
def writer_note(w: World):
    return w.writer_note("覚書",
            )

def abstract(w: World):
    return w.writer_note('概要',
            )


def main(): # pragma: no cover
    w = World.create_world(f"{TITLE}")
    w.config.set_version(MAJOR, MINOR, MICRO)
    w.db.set_from_asset(basic.ASSET)
    w.db.set_from_asset(common_rubi.ASSET)
    w.db.set_from_asset(ASSET)
    # spec
    w.config.set_copy(f"{COPY}")
    w.config.set_oneline(f"{ONELINE}")
    w.config.set_outline(f"{OUTLINE}")
    w.config.set_theme(f"{THEME}")
    w.config.set_genre(f"{GENRE}")
    w.config.set_target(f"{TARGET}")
    w.config.set_size(f"{SIZE}")
    w.config.set_contest_info(f"{CONTEST_INFO}")
    w.config.set_caution(f"{CAUTION}")
    w.config.set_note(f"{NOTE}")
    w.config.set_sites(*SITES)
    w.config.set_released(*RELEASED)
    return w.run(
            abstract(w),
            ch_main(w),
            )


if __name__ == '__main__':
    import sys
    sys.exit(main())

