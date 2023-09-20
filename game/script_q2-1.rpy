label q2_1:
    chi_speaking "你好~又见面啦，我说的没错吧！"
    qian_speaking "……\n是啊。请问这次的故障问题是什么？现在机器不在这边吗？"
    chi_speaking "对呀……出了点意外，可能要晚点才能送过来了，不好意思啊。"
    qian_speaking "嗯，这个没事的……不过，如果不着急的话，可以在东西到这里之后再联系公司，这样也不用麻烦你等在这里。"
    chi_speaking "不麻烦啊，我们可以先做点别的。"
    qian "她捏捏垂下的发尾，面上带笑地看着我，水色的眼眸里就像在闪动真正的水波，名为好奇。\n我有些受不了这样直接的目光，稍稍瞥开了眼睛。"
    qian_speaking "是，是吗……"
    chi_speaking "就随便聊聊嘛。\n啊，对了，要不你帮我尝尝这个味道怎么样？"
    qian "可是——\n我的话还没说出口，被她递过来的一杯饮料堵住。\n淡淡的香甜气味让喉咙不自觉变紧，到D层之后，我很久没接触过鲜活的食物。\n难以拒绝…"
    chi_speaking "感觉怎么样？"
    qian_speaking "呃，挺好的。"
    qian "我唾弃这样装腔作势，故作深沉的自己，但还是刻意压低了声音，生硬地回应。"
    chi_speaking "太好了，谢谢你！"
    qian_speaking "也没什么……"
    qian_speaking "咦，机器还没送到吗？"
    chi_speaking "我看看哦……好像因为别的事情耽误了，大概还要一会儿。"
    qian_speaking "这样啊……"
    qian "我在心里叹了口气，一时间竟然不知道怎么接话，只好又调出那张通行证的信息。"
    chi_speaking "对哦，好可惜……那只能下次再找人了。\n不过，来A层也要不少时间，为什么不在这边多待一会？这样你们也不用那么辛苦了。"
    qian_speaking "……"
    qian "迟玉虽然这么说，脸上却看不出可惜，只是好奇。我突然后知后觉地意识到，自己面对她时感到的不和谐感。"
    qian "一种我以前很熟悉，而现在逐渐消解的天真。"
    qian "面对那汪清澈的浅蓝色湖水，我实在很难回答她。"

    qian "回到房间，我查看光屏页面的时候，联系人的头像闪了闪，是迟玉发来的消息。"
    # screen mode
    chi_speaking "谢谢你今天陪我聊天^_^"
    chi_speaking "下次我再找你过来玩吧"
    chi_speaking "机器也还没有修好呢"
    qian_speaking "好的"
    qian_speaking "我会帮你解决问题"
    chi_speaking "其实你只要过来陪我待着就好啦"

    qian "……\n她毫不掩饰自己有其他目的——对A层的人来说，随意使用他人的确是一种日常。\n只是，我到D层后才知道原来其他人是不一样的。"
    qian "……似乎有些难受。\n然而我又同时意识到，这对我来说是个极好的机会——迟玉是A区人，对我大概印象不差，看起来天真善良……"
    
    qian_speaking "好啊^_^"

    qian "啊，我也终于想到这一层了……"
    chi_speaking "待会我还有事"
    chi_speaking "那，之后我再找机会让你过来哦"
    qian_speaking "嗯嗯^_^"

    qian "不过……为什么是找机会？我没有去深究，眼下更重要的是……我似乎已经取得了不错的进展——在和迟玉的接触上。"
    qian "那之后……？"

    menu:
        "【和她继续保持关系】":
            jump q2_1_1
        "【找她打听家里人的情况】":
            jump q2_1_2


label q2_1_1:
    qian "不，现在就直接说可能还是太激进了……A层的人不管是谁，在身份上都会对现在的我带来危险。"
    qian "还是先和她保持联系，多接触一段时间，从别的地方观察一下吧……"
    qian_speaking "迟玉……"
    unknown "你是，在说迟玉嘛？"
    qian_speaking "啊？是，怎么了……"
    qian "我没想到自言自语会被人听到，还是没说过话的同事，一时有些摸不着头脑。"
    coworker_speaking "就八卦呗，你们小年轻还知道这个人？最近又有她的消息了？那孩子可真是个厉害的……"
    qian_speaking "呃，那个，什么……"
    coworker_speaking "说实在的，年轻人还是要做到她那样啊，D层出生的，一路往上爬到那么高，当记者采访蓝石还能被看中，是真厉害……不过到A层就没消息了，估计也是看不上咱们这。"
    qian "等等，这是什么意思……她和我好像完全不在说同一件事，可……让我很在意。"
    qian_speaking "诶，那是……那是什么时候的事？"
    coworker_speaking "哎？合着你不知道啊？我就说嘛……那你在这嘀咕啥呢？"
    qian_speaking "不是！我是听家里人说过，但是没说过具体的事情……"
    coworker_speaking "这样啊，的确是你们的榜样，可以讲讲的。我想想啊……那是二十多年前的事吧，蓝石科技刚做起来，特别厉害，迟玉也抓住了这个机会啊，出了特别多报道。"
    coworker_speaking "说实在的，我感觉那报道她没发挥好，不是以前的风格，但人家就是厉害，换了风格也能被蓝石看中，就带到A层去了。然后咱们就不知道喽，不过A层肯定哪哪都好啊。"
    coworker_speaking "不过啊，虽然咱嫉妒，但也得恭喜她……后来D层越来越乱，咱们都快活不下去了，看着有人离开也好啊……"
    coworker_speaking "行了行了，我讲这么多干啥……工作，工作去了。"
    qian_speaking "这，这样啊……谢谢……"
    qian "二十多年前，那肯定不是现在的迟玉……她看起来最多也就十八岁吧，和我一样大……可是同样的名字，同样和蓝石有关，怎么看都觉得很奇怪……"
    qian "奇怪了，这似乎和我也没什么关系，为什么想到那张笑脸和那双水蓝色的眼睛，心里还是生出难以言喻的难过。"
    qian "这样的事情，还是不跟她讨论了……"
    qian "阳光明媚，今天荆棘之城的天气设定是晴天。满是落地窗的一层小楼被打理得精致有序，人造光线透过雕花玻璃映出好看的形状，在迟玉的额角留下一抹光晕。"

    #TODO: 转场
    qian "我怀念这样久违的，温暖平和的环境，一瞬间竟然看得有些痴迷了。"
    chi_speaking "你在看什么，有什么特别的吗？"
    qian_speaking "啊，没，就是觉得你这环境挺好的……"
    chi_speaking "你喜欢啊？那你多来玩呀。"
    qian_speaking "那不太行啦……"
    chi_speaking "是来A层太远太累了吗？"
    qian_speaking "也不算吧，就是，不太方便……"
    chi_speaking "那我就说要维修机器，然后每次找你过来就行了呗。"
    qian_speaking "……所以你根本没想着要我修机器啊。"
    chi_speaking "嘿嘿。"
    qian "迟玉眨了眨眼，没有否认的意思，只是笑着看我。裙摆和胸口的的花边随着她一起轻轻摇晃，划出漂亮的旋律，引我想要合唱——但还是止住了任何向外飘逸的想法。"
    chi_speaking "反正不管用什么理由，能把你叫来就行啦。只要我说一下，又不会有人拒绝我，真的很方便呢！"
    qian "的确，是A区的话，大多数人都不可能会拒绝……\n这对我来说算是好消息，但我却莫名有种堵着的感觉。"
    qian_speaking "好啊，那我尽量来找你。"
    chi_speaking "那就很好啦。"
    chi_speaking "哎，你身上怎么都湿了？快过来我帮你擦一下。"
    #TODO: 转场
    qian_speaking "啊不用……啊，呃……谢谢。"
    qian "迟玉围着我转圈，把我身上的水汽都擦掉。柔软的发丝和宽大的裙摆时不时扫过我的皮肤，让我动也不敢动，只是僵硬在原地。"
    chi_speaking "你也很喜欢雨吗？不过就算喜欢，也不能特地跑出去淋湿啊。"
    qian_speaking "我可没有特地跑出去……这么大的雨，走在路上就是会打湿的，所以其实没事的，不用帮我擦……"
    chi_speaking "什么啊，不都是有雨雪通道的吗，你不走才会被淋湿啊。"
    qian_speaking "……D层没有那些东西的，总之，不太方便吧……"
    chi_speaking "啊？这样吗？那真的很麻烦诶……"
    qian_speaking "嗯……"
    qian "我的心绪忽然沉下来，这是怎么了……简直就像这天气似的，阴晴不定，叫我感觉麻烦又难受。"
    chi_speaking "唉，偶尔我也想自己出去啊，也不用总是找借口让你过来……什么时候会有那一天呢？"
    #TODO: 转场
    qian_speaking "诶……啊。那个……不能出去么？"
    qian "迟玉那明显不同于平时的情绪令我有些不安，我顿了顿，摸不准她的意思，只好小心地试探。"
    chi_speaking "是啊，我，我的母亲，她不让我去外面的地方。她说外面太危险了，不适合我，我只要待在家里就好……"
    chi_speaking "可能她也有没告诉我的理由，但我有时候还是会想……啊，我是不是说太多无聊的事了。"
    qian_speaking "怎么会这样……没事，你说什么都可以。"
    qian "我很想说什么，说出的的话却干巴巴的。"
    chi_speaking "……所以，你能来这里陪我，我真的很开心。\n谢谢你哦，时茜。至少现在你在这里，我……那个，我很幸运……"
    qian "什么啊……为什么看到她泛红的脸颊，我的面部也隐隐做烧起来……"
    qian "不行，我想要说点什么来转移话题……"
    menu:
        "【衣服好看】":
            qian "那个，你的衣服很好看啊，感觉很适合你。"
            qian "许久没有机会说这些话，我十分笨拙地在脑内搜刮恰当的词汇，话题实在生硬。"
            qian "迟玉似乎完全不在意我的卡壳，而是十分开心地接了话。和我不同，她的笑容是如此明朗，不含任何杂质与阴霾，比阳光更甚，驱散我身上的水汽。"
            chi_speaking "这是……我妈妈买给我的，很好看吗？"
            qian_speaking "是啊。"
            chi_speaking "谢谢你，我也觉得很好看，但还是第一次有别人这么说。"
            qian "迟玉站起身转了个圈，裙摆再次跟着她的动作一起跳舞，每个节拍都恰好踩在我心跳的节奏。"
            chi_speaking "时茜，我好开心！"
            qian_speaking "嗯。"
            qian "不自觉，我的语气也被她所感染，变得轻快起来。"
    
    menu:
        "【眼睛漂亮】":
            qian "那个，我一直觉得你的眼睛很漂亮，感觉和这种天气很像，但更好看……啊。"
            qian "这转折似乎太生硬了些……但我没能继续想下去，因为迟玉的表情突然暗淡了。"
            chi_speaking "抱，抱歉……我的眼睛不好看的，可以不要这么仔细看吗……"
            qian_speaking "你怎么会这么想——"
            chi_speaking "真的不好看……\n真对不起，说这些扫兴的话。"
            qian_speaking "没有的事……我没有别的想法，只是想夸你好看。\n我，我是真心的，那个……"
            chi_speaking "……真的吗？我的眼睛，不丑吗？"
            qian_speaking "当然不丑！"
            chi_speaking "……这样啊。"
            qian "迟玉只是轻轻呢喃，没有继续说话。我顿了顿，心底突然生起勇气。"
            qian_speaking "我！我就很喜欢你……你的眼睛。"
            chi_speaking "……我，我也是……我喜欢，你，你的眼睛。"
            qian "我的耳朵突然开始轰鸣，像是被不真实的泡沫包裹，淹没。虽然不真实，却令人难以逃脱。"
    

    chi_speaking "今天我做了新的口味哦，这杯饮料里加了点荆棘花瓣！"
    #TODO: 转场，cg？
    qian_speaking "荆棘花还能用来做调料吗？嗯……好像没什么特别的味道，挺好喝的。"
    chi_speaking "第一次尝试啦，因为我很喜欢这朵花嘛。"
    qian_speaking "是哦，听说以前在大家快饿死的时候就是吃荆棘花活下来的，因为有荆棘花和那时候坚持的人才有现在的城市，真的很……"
    "叮，叮——"
    chi_speaking "咦，怎么会有人来？啊……"
    qian "我的话被突兀的门铃声打断，而迟玉的惊呼让我也不由得开始紧张。余光里的影子在靠近，逐渐和迟玉的影子融为一体。我把脊背用力绷直，假装在认真工作对谈。"
    unknown "这位是？"
    chi_speaking "啊！她是——"
    qian_speaking "我是来处理订单问题的，刚刚正在讨论……啊，您好。"
    unknown "你好啊，看样子你认识我？"
    qian_speaking "没有人不认识您吧。"
    qian "蓝石，“那个”蓝石——荆棘之城最出名的人物之一，名下有多个科技产业和慈善基金，创造了无数工作岗位，是备受喜爱的成功人士。"
    lan_speaking "哈哈，那就有些夸张了。我早就比不上你们这些年轻人了，来这里工作很辛苦吧，迟玉给你添麻烦了。"
    qian_speaking "没有的事……"
    lan_speaking "现在是还有什么问题吗？"
    qian_speaking "不，没有……我们基本谈好了。"
    lan_speaking "嗯。"
    lan_speaking "如果还有别的事情，也尽快解决吧。迟玉……她该休息了。"
    qian_speaking "没有了……那，我就先离开了。"
    qian "不知道是不是我的错觉，和节目上看的不同，蓝石虽然笑得温和，却给人一种无形的压力。也许，是因为我似乎能隐约感觉到……她很想让我快点走。"
    qian "不过，她似乎和迟玉过分熟稔，如果关系亲密，接近迟玉也许可以再和蓝石交好，说不定对我有大帮助……"
    chi_speaking "……要走了吗？"
    lan_speaking "是啊，迟玉还有什么事吗？"
    chi_speaking "不……那，拜拜。"
    qian_speaking "……\n感谢您配合我们的工作，如果有问题随时联系公司。…"
    qian "蓝石是生气了吗？会影响到迟玉吗？我还能……见到她吗？\n我的内心突然十分紧张，为什么……一定是因为害怕影响到我之后的工作和计划……"
    qian "一定是这样……所以才让我现在还想再看她一眼。"
    qian "想到这里，我的脚步顿了顿，才发现自己走得很慢，现在刚离开院子的门口而已。既然这样，那就刚好再看一眼……\n……嗯……？这是……"
    qian "呼……哈啊……因为剧烈跑步，我停下来之后还止不住喘息。血液在血管里高速流动，让我的思绪更加活跃。先前看到的画面在大脑里不断闪回，我无法理解，又忍不住来回回想。"
    #TODO: 转场
    qian "那是什么情况？蓝石的动作超出我的预料，我不明白，亲人之间，或者家人之间，应该是那样的吗？……我不懂，甚至，我现在连我自己都不太懂了……为什么我要那么着急跑开？为什么我会难受？"
    #TODO: cg
    qian "胃部感到难受，像是什么东西搅在一起，有些酸，有些痛……\n到最后，所有的思绪融化成下意识的自言自语。\n迟玉……"
    unknown "时茜小姐，有人找你。"
    #TODO: 转场
    qian_speaking "什么？"
    qian "我惊讶于别人礼貌的口气，也不认为到了D层之后，会有什么人特意来这里找我。\n但听到那人的名字后，不知道为何，一种“果然”的感觉油然而生。"
    qian_speaking "好，我知道了。"
    qian "蓝石……默念这个名字的时候，我的心底泛上一阵莫名的疼痛，说不清楚，却令我难受不已。"
    qian "脑袋控制不住地涌上回忆的景象，不断靠近的身体，抚摸，触碰，如提线木偶般的动作，往下，向上。"
    qian "一边是我从小尊敬的人，一边是……迟玉——我不知道，该如何形容她——不论是谁我都不想有不好的猜测。可现在，我的思绪却持续飘得越来越远，越来越乱。"
    qian "迟玉……你为什么？"
    unknown "您在听吗？"
    qian_speaking "啊，不好意思……蓝石女士她，现在在外面是吗。"
    unknown "不是，但她需要你去一个地方。"
    qian_speaking "好的……"
    qian "这是个宽敞整洁的房间，家具是统一的银白色，摆放得整整齐齐。我有些局促地站在门口，和周围格格不入。\n私人载具竟然能有这么大位置，不愧是蓝石科技……"
    #TODO: 转场
    qian_speaking "那个……"
    unknown "请在里面等一会，之后会有人来找你。"
    qian_speaking "好的……"
    qian "门关上了，只剩死一样的安静。我有些不安，不知道即将到来的是什么。\n……是因为发现我看到了那件事吗？还是因为认出了我，会说什么吗？"
    qian "……"
    unknown "茜……时茜……"
    qian_speaking "……谁？是有人在叫我吗？……我——唔唔唔！！"
    chi_speaking "小声点……你果然在里面啊。"
    qian_speaking "你怎么来了？！怎，怎么了吗？"
    chi_speaking "我——我想见你。"
    qian "……什么？\n那一瞬间，我的大脑有些空白，无法理解这语句的含义。从耳郭开始，热意向内扩散，烧得我脑袋嗡嗡作响。"
    qian_speaking "那，那个，什么意思……呃，你，我……"
    chi_speaking "呼……累死我了……我，好不容易过来……\n那个，啊……你相信我吗？"
    qian "——你相信我吗？\n没头没尾，如此突兀的一句话。"
    qian_speaking "等等，那是……什么意思啊？"
    chi_speaking "没什么啦，我只是突然好奇……不过你就告诉我嘛……你会吗？不管我说什么……你会相信我说的话吗？你会相信我吗？"
    qian "这……\n我从未见过迟玉这样的表情。\n她并不说别的，只是直直地盯着我，仿佛非要我说出一个结果。"
    qian "我……"
    menu:
        "【相信她】":
            jump q2_1_1_1
        "【不相信她】":
            jump q2_1_1_2




label q2_1_2:
    qian "这么说来，正好可以问问家里人的情况，不知道黄女士和钟女士怎么样了……\n我稍微思虑一下，便下定决心，打开和迟玉的对话框。"

    qian_speaking "如果方便的话，能向你打听个人吗"
    qian_speaking "也是A区的，我想你可能会熟悉"
    chi_speaking "没问题，你告诉我吧"
    chi_speaking "其实我也不认识什么人，不过我会帮你问到的^ ^"
    qian_speaking "谢谢你！"
    qian "无论如何，至少这句话我是发自真心……我还真是卑鄙。"

    qian "没有新的消息。"
    qian "自从那天过后，迟玉就没有再回复过我，我心里焦虑，却没法跟别人说，更没办法直接催她，只好每天数着数过日子。"
    qian "但我没想到，在她之前，有其他人先行找上门。"

    stf_speaking "时茜小姐，有人找你。"
    