
import pickle

# Data sets recovered from the functions within dataManipulation and generateDistribution.py.
# To update, run the corresponding functions, copy and paste the output into the corresponding variable, and run this file.

prefecture_city_list = [
    
   
  [
    "Nagoya",
    [
      "35.183",
      "136.900"
    ],
    "Aichi Prefecture"
  ],
  [
    "Toyohashi",
    [
      "34.76917",
      "137.391528"
    ],
    "Aichi Prefecture"
  ],
  [
    "Okazaki, Aichi",
    [
      "34.954333",
      "137.174361"
    ],
    "Aichi Prefecture"
  ],
  [
    "Ichinomiya, Aichi",
    [
      "35.30389",
      "136.80306"
    ],
    "Aichi Prefecture"
  ],
  [
    "Seto, Aichi",
    [
      "35.223583",
      "137.084194"
    ],
    "Aichi Prefecture"
  ],
  [
    "Handa, Aichi",
    [
      "34.89194",
      "136.93806"
    ],
    "Aichi Prefecture"
  ],
  [
    "Kasugai, Aichi",
    [
      "35.24750",
      "136.97222"
    ],
    "Aichi Prefecture"
  ],
  [
    "Toyokawa, Aichi",
    [
      "34.826778",
      "137.375917"
    ],
    "Aichi Prefecture"
  ],
  [
    "Tsushima, Aichi",
    [
      "35.177056",
      "136.741278"
    ],
    "Aichi Prefecture"
  ],
  [
    "Hekinan",
    [
      "34.884694",
      "136.993417"
    ],
    "Aichi Prefecture"
  ],
  [
    "Kariya, Aichi",
    [
      "34.989278",
      "137.002139"
    ],
    "Aichi Prefecture"
  ],
  [
    "Toyota, Aichi",
    [
      "35.082444",
      "137.156333"
    ],
    "Aichi Prefecture"
  ],
  [
    "Anj\u014d",
    [
      "34.958722",
      "137.080333"
    ],
    "Aichi Prefecture"
  ],
  [
    "Nishio",
    [
      "34.833",
      "137.067"
    ],
    "Aichi Prefecture"
  ],
  [
    "Gamag\u014dri",
    [
      "34.84306",
      "137.219583"
    ],
    "Aichi Prefecture"
  ],
  [
    "Inuyama, Aichi",
    [
      "35.37861",
      "136.944500"
    ],
    "Aichi Prefecture"
  ],
  [
    "Tokoname",
    [
      "34.886528",
      "136.832333"
    ],
    "Aichi Prefecture"
  ],
  [
    "K\u014dnan, Aichi",
    [
      "35.332083",
      "136.870667"
    ],
    "Aichi Prefecture"
  ],
  [
    "Komaki",
    [
      "35.291000",
      "136.912111"
    ],
    "Aichi Prefecture"
  ],
  [
    "Inazawa",
    [
      "35.26472",
      "136.796917"
    ],
    "Aichi Prefecture"
  ],
  [
    "T\u014dkai, Aichi",
    [
      "35.02306",
      "136.902194"
    ],
    "Aichi Prefecture"
  ],
  [
    "\u014cbu",
    [
      "35.01167",
      "136.963667"
    ],
    "Aichi Prefecture"
  ],
  [
    "Chita, Aichi",
    [
      "35.000",
      "136.867"
    ],
    "Aichi Prefecture"
  ],
  [
    "Chiry\u016b",
    [
      "35.00139694",
      "137.0506028"
    ],
    "Aichi Prefecture"
  ],
  [
    "Owariasahi",
    [
      "35.216528",
      "137.035361"
    ],
    "Aichi Prefecture"
  ],
  [
    "Takahama, Aichi",
    [
      "34.92750",
      "136.98778"
    ],
    "Aichi Prefecture"
  ],
  [
    "Iwakura, Aichi",
    [
      "35.27944",
      "136.871417"
    ],
    "Aichi Prefecture"
  ],
  [
    "Toyoake",
    [
      "35.050861",
      "137.012833"
    ],
    "Aichi Prefecture"
  ],
  [
    "Nisshin, Aichi",
    [
      "35.131972",
      "137.03944"
    ],
    "Aichi Prefecture"
  ],
  [
    "Tahara, Aichi",
    [
      "34.668750",
      "137.280889"
    ],
    "Aichi Prefecture"
  ],
  [
    "Aisai",
    [
      "35.15278",
      "136.728222"
    ],
    "Aichi Prefecture"
  ],
  [
    "Kiyosu",
    [
      "35.199806",
      "136.852861"
    ],
    "Aichi Prefecture"
  ],
  [
    "Shinshiro",
    [
      "34.915917",
      "137.49861"
    ],
    "Aichi Prefecture"
  ],
  [
    "Kitanagoya",
    [
      "35.245639",
      "136.865944"
    ],
    "Aichi Prefecture"
  ],
  [
    "Yatomi",
    [
      "35.117",
      "136.717"
    ],
    "Aichi Prefecture"
  ],
  [
    "Miyoshi, Aichi",
    [
      "35.08944",
      "137.074833"
    ],
    "Aichi Prefecture"
  ],
  [
    "Ama, Aichi",
    [
      "35.200444",
      "136.783222"
    ],
    "Aichi Prefecture"
  ],
  [
    "Nagakute",
    [
      "35.184000",
      "137.048694"
    ],
    "Aichi Prefecture"
  ],
  [
    "Akita, Akita",
    [
      "39.720028",
      "140.102583"
    ],
    "Akita Prefecture"
  ],
  [
    "\u014cdate, Akita",
    [
      "40.27139",
      "140.56417"
    ],
    "Akita Prefecture"
  ],
  [
    "Kazuno, Akita",
    [
      "40.215778",
      "140.7883778"
    ],
    "Akita Prefecture"
  ],
  [
    "Daisen, Akita",
    [
      "39.45306",
      "140.475444"
    ],
    "Akita Prefecture"
  ],
  [
    "Katagami, Akita",
    [
      "39.883222",
      "139.988583"
    ],
    "Akita Prefecture"
  ],
  [
    "Kitaakita, Akita",
    [
      "40.226028",
      "140.370806"
    ],
    "Akita Prefecture"
  ],
  [
    "Oga, Akita",
    [
      "39.886833",
      "139.847583"
    ],
    "Akita Prefecture"
  ],
  [
    "Yurihonj\u014d, Akita",
    [
      "39.385861",
      "140.048833"
    ],
    "Akita Prefecture"
  ],
  [
    "Yuzawa, Akita",
    [
      "39.164083",
      "140.494833"
    ],
    "Akita Prefecture"
  ],
  [
    "Semboku, Akita",
    [
      "39.70167",
      "140.731500"
    ],
    "Akita Prefecture"
  ],
  [
    "Yokote, Akita",
    [
      "39.311333",
      "140.553278"
    ],
    "Akita Prefecture"
  ],
  [
    "Nikaho, Akita",
    [
      "39.203000",
      "139.907750"
    ],
    "Akita Prefecture"
  ],
  [
    "Noshiro, Akita",
    [
      "40.212139",
      "140.026611"
    ],
    "Akita Prefecture"
  ],
  [
    "Hachinohe",
    [
      "40.512278",
      "141.488389"
    ],
    "Aomori Prefecture"
  ],
  [
    "Kuroishi, Aomori",
    [
      "40.642611",
      "140.611306"
    ],
    "Aomori Prefecture"
  ],
  [
    "Misawa, Aomori",
    [
      "40.683083",
      "141.369056"
    ],
    "Aomori Prefecture"
  ],
  [
    "Mutsu, Aomori",
    [
      "41.292833",
      "141.18361"
    ],
    "Aomori Prefecture"
  ],
  [
    "Towada",
    [
      "40.612694",
      "141.205861"
    ],
    "Aomori Prefecture"
  ],
  [
    "Tsugaru, Aomori",
    [
      "40.808722",
      "140.380056"
    ],
    "Aomori Prefecture"
  ],
  [
    "Goshogawara",
    [
      "40.808028",
      "140.440083"
    ],
    "Aomori Prefecture"
  ],
  [
    "Aomori",
    [
      "40.82278",
      "140.74694"
    ],
    "Aomori Prefecture"
  ],
  [
    "Hirakawa, Aomori",
    [
      "40.584111",
      "140.566472"
    ],
    "Aomori Prefecture"
  ],
  [
    "Hirosaki",
    [
      "40.603111",
      "140.463833"
    ],
    "Aomori Prefecture"
  ],
  [
    "Chiba, Chiba",
    [
      "35.607278",
      "140.106361"
    ],
    "Chiba Prefecture"
  ],
  [
    "Ch\u014dshi, Chiba",
    [
      "35.734639",
      "140.826778"
    ],
    "Chiba Prefecture"
  ],
  [
    "Ichikawa, Chiba",
    [
      "35.721917",
      "139.931056"
    ],
    "Chiba Prefecture"
  ],
  [
    "Funabashi, Chiba",
    [
      "35.694556",
      "139.982556"
    ],
    "Chiba Prefecture"
  ],
  [
    "Tateyama, Chiba",
    [
      "34.996583",
      "139.869972"
    ],
    "Chiba Prefecture"
  ],
  [
    "Kisarazu, Chiba",
    [
      "35.375972",
      "139.916833"
    ],
    "Chiba Prefecture"
  ],
  [
    "Matsudo, Chiba",
    [
      "35.787639",
      "139.903167"
    ],
    "Chiba Prefecture"
  ],
  [
    "Noda, Chiba",
    [
      "35.950",
      "139.867"
    ],
    "Chiba Prefecture"
  ],
  [
    "Mobara, Chiba",
    [
      "35.428528",
      "140.28806"
    ],
    "Chiba Prefecture"
  ],
  [
    "Narita, Chiba",
    [
      "35.77667",
      "140.31833"
    ],
    "Chiba Prefecture"
  ],
  [
    "Sakura, Chiba",
    [
      "35.717",
      "140.217"
    ],
    "Chiba Prefecture"
  ],
  [
    "T\u014dgane, Chiba",
    [
      "35.559944",
      "140.366083"
    ],
    "Chiba Prefecture"
  ],
  [
    "Narashino, Chiba",
    [
      "35.680389",
      "140.026500"
    ],
    "Chiba Prefecture"
  ],
  [
    "Kashiwa, Chiba",
    [
      "35.867583",
      "139.975750"
    ],
    "Chiba Prefecture"
  ],
  [
    "Katsuura, Chiba",
    [
      "35.150",
      "140.317"
    ],
    "Chiba Prefecture"
  ],
  [
    "Ichihara, Chiba",
    [
      "35.49806",
      "140.115444"
    ],
    "Chiba Prefecture"
  ],
  [
    "Nagareyama, Chiba",
    [
      "35.856306",
      "139.902861"
    ],
    "Chiba Prefecture"
  ],
  [
    "Yachiyo, Chiba",
    [
      "35.722417",
      "140.099889"
    ],
    "Chiba Prefecture"
  ],
  [
    "Abiko, Chiba",
    [
      "35.867",
      "140.033"
    ],
    "Chiba Prefecture"
  ],
  [
    "Kamagaya, Chiba",
    [
      "35.776833",
      "140.000806"
    ],
    "Chiba Prefecture"
  ],
  [
    "Kimitsu, Chiba",
    [
      "35.3304500",
      "139.9026778"
    ],
    "Chiba Prefecture"
  ],
  [
    "Futtsu, Chiba",
    [
      "35.304083",
      "139.857028"
    ],
    "Chiba Prefecture"
  ],
  [
    "Urayasu, Chiba",
    [
      "35.653944",
      "139.902167"
    ],
    "Chiba Prefecture"
  ],
  [
    "Yotsukaid\u014d, Chiba",
    [
      "35.669778",
      "140.167944"
    ],
    "Chiba Prefecture"
  ],
  [
    "Sodegaura, Chiba",
    [
      "35.43000",
      "139.954417"
    ],
    "Chiba Prefecture"
  ],
  [
    "Yachimata, Chiba",
    [
      "35.667",
      "140.317"
    ],
    "Chiba Prefecture"
  ],
  [
    "Inzai, Chiba",
    [
      "35.833",
      "140.150"
    ],
    "Chiba Prefecture"
  ],
  [
    "Shiroi, Chiba",
    [
      "35.791472",
      "140.056306"
    ],
    "Chiba Prefecture"
  ],
  [
    "Tomisato, Chiba",
    [
      "35.700",
      "140.567"
    ],
    "Chiba Prefecture"
  ],
  [
    "Kamogawa, Chiba",
    [
      "35.114028",
      "140.09889"
    ],
    "Chiba Prefecture"
  ],
  [
    "Asahi, Chiba",
    [
      "35.717",
      "140.650"
    ],
    "Chiba Prefecture"
  ],
  [
    "Isumi, Chiba",
    [
      "35.253917",
      "140.385194"
    ],
    "Chiba Prefecture"
  ],
  [
    "S\u014dsa, Chiba",
    [
      "35.70750",
      "140.56417"
    ],
    "Chiba Prefecture"
  ],
  [
    "Minamib\u014ds\u014d, Chiba",
    [
      "35.043167",
      "139.84000"
    ],
    "Chiba Prefecture"
  ],
  [
    "Katori, Chiba",
    [
      "35.683",
      "140.033"
    ],
    "Chiba Prefecture"
  ],
  [
    "Sanmu, Chiba",
    [
      "35.600",
      "140.417"
    ],
    "Chiba Prefecture"
  ],
  [
    "\u014camishirasato, Chiba",
    [
      "35.517",
      "140.317"
    ],
    "Chiba Prefecture"
  ],
  [
    "Matsuyama",
    [
      "33.833",
      "132.767"
    ],
    "Ehime Prefecture"
  ],
  [
    "Niihama",
    [
      "33.967",
      "133.283"
    ],
    "Ehime Prefecture"
  ],
  [
    "Shikokuch\u016b\u014d",
    [
      "33.983",
      "133.550"
    ],
    "Ehime Prefecture"
  ],
  [
    "Seiyo, Ehime",
    [
      "33.36278",
      "132.51083"
    ],
    "Ehime Prefecture"
  ],
  [
    "T\u014don, Ehime",
    [
      "33.783",
      "132.867"
    ],
    "Ehime Prefecture"
  ],
  [
    "Saij\u014d, Ehime",
    [
      "33.917",
      "133.183"
    ],
    "Ehime Prefecture"
  ],
  [
    "\u014czu, Ehime",
    [
      "33.500",
      "132.550"
    ],
    "Ehime Prefecture"
  ],
  [
    "Imabari, Ehime",
    [
      "34.067",
      "133.000"
    ],
    "Ehime Prefecture"
  ],
  [
    "Yawatahama",
    [
      "33.467",
      "132.417"
    ],
    "Ehime Prefecture"
  ],
  [
    "Iyo, Ehime",
    [
      "33.750",
      "132.700"
    ],
    "Ehime Prefecture"
  ],
  [
    "Uwajima, Ehime",
    [
      "33.217",
      "132.567"
    ],
    "Ehime Prefecture"
  ],
  [
    "Fukui (city)",
    [
      "36.064056",
      "136.219583"
    ],
    "Fukui Prefecture"
  ],
  [
    "Tsuruga, Fukui",
    [
      "35.645194",
      "136.055500"
    ],
    "Fukui Prefecture"
  ],
  [
    "Obama, Fukui",
    [
      "35.495667",
      "135.746611"
    ],
    "Fukui Prefecture"
  ],
  [
    "\u014cno, Fukui",
    [
      "35.97972",
      "136.48750"
    ],
    "Fukui Prefecture"
  ],
  [
    "Katsuyama, Fukui",
    [
      "36.060861",
      "136.500639"
    ],
    "Fukui Prefecture"
  ],
  [
    "Sabae, Fukui",
    [
      "35.956472",
      "136.184278"
    ],
    "Fukui Prefecture"
  ],
  [
    "Awara, Fukui",
    [
      "36.211306",
      "136.228972"
    ],
    "Fukui Prefecture"
  ],
  [
    "Echizen, Fukui",
    [
      "35.903500",
      "136.168750"
    ],
    "Fukui Prefecture"
  ],
  [
    "Sakai, Fukui",
    [
      "36.16694",
      "136.231444"
    ],
    "Fukui Prefecture"
  ],
  [
    "Fukuoka",
    [
      "33.583",
      "130.400"
    ],
    "Fukuoka Prefecture"
  ],
  [
    "Kurume, Fukuoka",
    [
      "33.317",
      "130.517"
    ],
    "Fukuoka Prefecture"
  ],
  [
    "\u014cmuta, Fukuoka",
    [
      "33.033",
      "130.450"
    ],
    "Fukuoka Prefecture"
  ],
  [
    "N\u014dgata, Fukuoka",
    [
      "33.74167",
      "130.73222"
    ],
    "Fukuoka Prefecture"
  ],
  [
    "Tagawa, Fukuoka",
    [
      "33.63889",
      "130.80611"
    ],
    "Fukuoka Prefecture"
  ],
  [
    "Yanagawa, Fukuoka",
    [
      "33.15972",
      "130.40806"
    ],
    "Fukuoka Prefecture"
  ],
  [
    "Yame, Fukuoka",
    [
      "33.19944",
      "130.55889"
    ],
    "Fukuoka Prefecture"
  ],
  [
    "Chikugo, Fukuoka",
    [
      "33.20917",
      "130.50444"
    ],
    "Fukuoka Prefecture"
  ],
  [
    "\u014ckawa, Fukuoka",
    [
      "33.200",
      "130.383"
    ],
    "Fukuoka Prefecture"
  ],
  [
    "Yukuhashi, Fukuoka",
    [
      "33.733",
      "130.983"
    ],
    "Fukuoka Prefecture"
  ],
  [
    "Buzen, Fukuoka",
    [
      "33.617",
      "131.133"
    ],
    "Fukuoka Prefecture"
  ],
  [
    "Nakagawa, Fukuoka",
    [
      "33.500",
      "130.417"
    ],
    "Fukuoka Prefecture"
  ],
  [
    "Nakama, Fukuoka",
    [
      "33.82083",
      "130.70833"
    ],
    "Fukuoka Prefecture"
  ],
  [
    "Kitakyushu",
    [
      "33.883",
      "130.883"
    ],
    "Fukuoka Prefecture"
  ],
  [
    "Og\u014dri, Fukuoka",
    [
      "33.400",
      "130.550"
    ],
    "Fukuoka Prefecture"
  ],
  [
    "Chikushino, Fukuoka",
    [
      "33.500",
      "130.517"
    ],
    "Fukuoka Prefecture"
  ],
  [
    "Kasuga, Fukuoka",
    [
      "33.533",
      "130.467"
    ],
    "Fukuoka Prefecture"
  ],
  [
    "\u014cnoj\u014d, Fukuoka",
    [
      "33.533",
      "130.483"
    ],
    "Fukuoka Prefecture"
  ],
  [
    "Munakata, Fukuoka",
    [
      "33.800",
      "130.533"
    ],
    "Fukuoka Prefecture"
  ],
  [
    "Dazaifu, Fukuoka",
    [
      "33.517",
      "130.517"
    ],
    "Fukuoka Prefecture"
  ],
  [
    "Koga, Fukuoka",
    [
      "33.733",
      "130.467"
    ],
    "Fukuoka Prefecture"
  ],
  [
    "Fukutsu, Fukuoka",
    [
      "33.767",
      "130.483"
    ],
    "Fukuoka Prefecture"
  ],
  [
    "Ukiha, Fukuoka",
    [
      "33.350",
      "130.750"
    ],
    "Fukuoka Prefecture"
  ],
  [
    "Miyawaka, Fukuoka",
    [
      "33.717",
      "130.667"
    ],
    "Fukuoka Prefecture"
  ],
  [
    "Asakura, Fukuoka",
    [
      "33.417",
      "130.667"
    ],
    "Fukuoka Prefecture"
  ],
  [
    "Iizuka, Fukuoka",
    [
      "33.650",
      "130.683"
    ],
    "Fukuoka Prefecture"
  ],
  [
    "Kama, Fukuoka",
    [
      "33.563250",
      "130.711806"
    ],
    "Fukuoka Prefecture"
  ],
  [
    "Miyama, Fukuoka",
    [
      "33.150",
      "130.467"
    ],
    "Fukuoka Prefecture"
  ],
  [
    "Itoshima, Fukuoka",
    [
      "33.55389",
      "130.19778"
    ],
    "Fukuoka Prefecture"
  ],
  [
    "Aizuwakamatsu, Fukushima",
    [
      "37.494833",
      "139.929750"
    ],
    "Fukushima Prefecture"
  ],
  [
    "Fukushima, Fukushima",
    [
      "37.760806",
      "140.47472"
    ],
    "Fukushima Prefecture"
  ],
  [
    "K\u014driyama, Fukushima",
    [
      "37.400444",
      "140.35972"
    ],
    "Fukushima Prefecture"
  ],
  [
    "Sukagawa, Fukushima",
    [
      "37.286472",
      "140.372667"
    ],
    "Fukushima Prefecture"
  ],
  [
    "S\u014dma, Fukushima",
    [
      "37.79667",
      "140.919639"
    ],
    "Fukushima Prefecture"
  ],
  [
    "Iwaki, Fukushima",
    [
      "37.050500",
      "140.887722"
    ],
    "Fukushima Prefecture"
  ],
  [
    "Tamura, Fukushima",
    [
      "37.433",
      "140.567"
    ],
    "Fukushima Prefecture"
  ],
  [
    "Shirakawa, Fukushima",
    [
      "37.126306",
      "140.210917"
    ],
    "Fukushima Prefecture"
  ],
  [
    "Nihonmatsu, Fukushima",
    [
      "37.584861",
      "140.431167"
    ],
    "Fukushima Prefecture"
  ],
  [
    "Minamis\u014dma, Fukushima",
    [
      "37.642194",
      "140.957306"
    ],
    "Fukushima Prefecture"
  ],
  [
    "Date, Fukushima",
    [
      "37.819139",
      "140.562972"
    ],
    "Fukushima Prefecture"
  ],
  [
    "Kitakata, Fukushima",
    [
      "37.651139",
      "139.874750"
    ],
    "Fukushima Prefecture"
  ],
  [
    "Motomiya, Fukushima",
    [
      "37.513194",
      "140.393833"
    ],
    "Fukushima Prefecture"
  ],
  [
    "Gifu, Gifu",
    [
      "35.423222",
      "136.760778"
    ],
    "Gifu Prefecture"
  ],
  [
    "\u014cgaki, Gifu",
    [
      "35.359361",
      "136.612861"
    ],
    "Gifu Prefecture"
  ],
  [
    "Takayama, Gifu",
    [
      "36.146028",
      "137.252167"
    ],
    "Gifu Prefecture"
  ],
  [
    "Tajimi, Gifu",
    [
      "35.33278",
      "137.131556"
    ],
    "Gifu Prefecture"
  ],
  [
    "Seki, Gifu",
    [
      "35.495778",
      "136.917972"
    ],
    "Gifu Prefecture"
  ],
  [
    "Nakatsugawa, Gifu",
    [
      "35.487583",
      "137.500583"
    ],
    "Gifu Prefecture"
  ],
  [
    "Mino, Gifu",
    [
      "35.544750",
      "136.907556"
    ],
    "Gifu Prefecture"
  ],
  [
    "Mizunami, Gifu",
    [
      "35.361806",
      "137.254500"
    ],
    "Gifu Prefecture"
  ],
  [
    "Hashima, Gifu",
    [
      "35.319944",
      "136.703278"
    ],
    "Gifu Prefecture"
  ],
  [
    "Minokamo, Gifu",
    [
      "35.440222",
      "137.015667"
    ],
    "Gifu Prefecture"
  ],
  [
    "Toki, Gifu",
    [
      "35.419194",
      "137.183250"
    ],
    "Gifu Prefecture"
  ],
  [
    "Kakamigahara, Gifu",
    [
      "35.398806",
      "136.848417"
    ],
    "Gifu Prefecture"
  ],
  [
    "Kani, Gifu",
    [
      "35.426056",
      "137.061333"
    ],
    "Gifu Prefecture"
  ],
  [
    "Yamagata, Gifu",
    [
      "35.50611",
      "136.781083"
    ],
    "Gifu Prefecture"
  ],
  [
    "Mizuho, Gifu",
    [
      "35.391806",
      "136.690861"
    ],
    "Gifu Prefecture"
  ],
  [
    "Hida, Gifu",
    [
      "36.238139",
      "137.186222"
    ],
    "Gifu Prefecture"
  ],
  [
    "Motosu, Gifu",
    [
      "35.483000",
      "136.678639"
    ],
    "Gifu Prefecture"
  ],
  [
    "Guj\u014d, Gifu",
    [
      "35.748556",
      "136.964333"
    ],
    "Gifu Prefecture"
  ],
  [
    "Gero, Gifu",
    [
      "35.805889",
      "137.244139"
    ],
    "Gifu Prefecture"
  ],
  [
    "Ena, Gifu",
    [
      "35.449250",
      "137.412833"
    ],
    "Gifu Prefecture"
  ],
  [
    "Kaizu, Gifu",
    [
      "35.22056",
      "136.636472"
    ],
    "Gifu Prefecture"
  ],
  [
    "Maebashi, Gunma",
    [
      "36.389500",
      "139.063417"
    ],
    "Gunma Prefecture"
  ],
  [
    "Takasaki, Gunma",
    [
      "36.321889",
      "139.003278"
    ],
    "Gunma Prefecture"
  ],
  [
    "Kiry\u016b, Gunma",
    [
      "36.405167",
      "139.497250"
    ],
    "Gunma Prefecture"
  ],
  [
    "Isesaki, Gunma",
    [
      "36.311361",
      "139.196806"
    ],
    "Gunma Prefecture"
  ],
  [
    "\u014cta, Gunma",
    [
      "36.291139",
      "139.375389"
    ],
    "Gunma Prefecture"
  ],
  [
    "Numata, Gunma",
    [
      "36.646028",
      "139.04417"
    ],
    "Gunma Prefecture"
  ],
  [
    "Tatebayashi, Gunma",
    [
      "36.244833",
      "139.542111"
    ],
    "Gunma Prefecture"
  ],
  [
    "Fujioka, Gunma",
    [
      "36.258694",
      "139.074556"
    ],
    "Gunma Prefecture"
  ],
  [
    "Shibukawa, Gunma",
    [
      "36.38944",
      "139.06333"
    ],
    "Gunma Prefecture"
  ],
  [
    "Annaka, Gunma",
    [
      "36.326250",
      "138.887139"
    ],
    "Gunma Prefecture"
  ],
  [
    "Tomioka, Gunma",
    [
      "36.259917",
      "138.889917"
    ],
    "Gunma Prefecture"
  ],
  [
    "Midori, Gunma",
    [
      "36.394806",
      "139.281139"
    ],
    "Gunma Prefecture"
  ],
  [
    "Hiroshima",
    [
      "34.39139",
      "132.45194"
    ],
    "Hiroshima Prefecture"
  ],
  [
    "Onomichi, Hiroshima",
    [
      "34.417",
      "133.200"
    ],
    "Hiroshima Prefecture"
  ],
  [
    "Kure, Hiroshima",
    [
      "34.24917",
      "132.56583"
    ],
    "Hiroshima Prefecture"
  ],
  [
    "Fukuyama, Hiroshima",
    [
      "34.48583",
      "133.36222"
    ],
    "Hiroshima Prefecture"
  ],
  [
    "Mihara, Hiroshima",
    [
      "34.39750",
      "133.07861"
    ],
    "Hiroshima Prefecture"
  ],
  [
    "Fuch\u016b, Hiroshima",
    [
      "34.56500",
      "133.24194"
    ],
    "Hiroshima Prefecture"
  ],
  [
    "Miyoshi, Hiroshima",
    [
      "34.800",
      "132.850"
    ],
    "Hiroshima Prefecture"
  ],
  [
    "Sh\u014dbara, Hiroshima",
    [
      "34.85444",
      "133.01917"
    ],
    "Hiroshima Prefecture"
  ],
  [
    "\u014ctake, Hiroshima",
    [
      "34.23778",
      "132.22222"
    ],
    "Hiroshima Prefecture"
  ],
  [
    "Takehara, Hiroshima",
    [
      "34.34167",
      "132.90694"
    ],
    "Hiroshima Prefecture"
  ],
  [
    "Higashihiroshima, Hiroshima",
    [
      "34.42639",
      "132.74333"
    ],
    "Hiroshima Prefecture"
  ],
  [
    "Hatsukaichi, Hiroshima",
    [
      "34.34833",
      "132.33167"
    ],
    "Hiroshima Prefecture"
  ],
  [
    "Akitakata, Hiroshima",
    [
      "34.66306",
      "132.70639"
    ],
    "Hiroshima Prefecture"
  ],
  [
    "Etajima, Hiroshima",
    [
      "34.217",
      "132.450"
    ],
    "Hiroshima Prefecture"
  ],
  [
    "Sapporo",
    [
      "43.067",
      "141.350"
    ],
    "Hokkaido",
    [
      "43",
      "142"
    ]
  ],
  [
    "Hakodate",
    [
      "41.76861",
      "140.72889"
    ],
    "Hokkaido",
    [
      "43",
      "142"
    ]
  ],
  [
    "Otaru",
    [
      "43.183",
      "141.000"
    ],
    "Hokkaido",
    [
      "43",
      "142"
    ]
  ],
  [
    "Asahikawa",
    [
      "43.767",
      "142.367"
    ],
    "Hokkaido",
    [
      "43",
      "142"
    ]
  ],
  [
    "Muroran",
    [
      "42.317",
      "140.967"
    ],
    "Hokkaido",
    [
      "43",
      "142"
    ]
  ],
  [
    "Obihiro",
    [
      "42.917",
      "143.200"
    ],
    "Hokkaido",
    [
      "43",
      "142"
    ]
  ],
  [
    "Y\u016bbari, Hokkaido",
    [
      "43.050",
      "141.967"
    ],
    "Hokkaido",
    [
      "43",
      "142"
    ]
  ],
  [
    "Iwamizawa",
    [
      "43.200",
      "141.783"
    ],
    "Hokkaido",
    [
      "43",
      "142"
    ]
  ],
  [
    "Abashiri",
    [
      "44.017",
      "144.267"
    ],
    "Hokkaido",
    [
      "43",
      "142"
    ]
  ],
  [
    "Rumoi, Hokkaido",
    [
      "43.933",
      "141.633"
    ],
    "Hokkaido",
    [
      "43",
      "142"
    ]
  ],
  [
    "Tomakomai",
    [
      "42.633",
      "141.600"
    ],
    "Hokkaido",
    [
      "43",
      "142"
    ]
  ],
  [
    "Wakkanai",
    [
      "45.415667",
      "141.67306"
    ],
    "Hokkaido",
    [
      "43",
      "142"
    ]
  ],
  [
    "Bibai",
    [
      "43.333",
      "141.850"
    ],
    "Hokkaido",
    [
      "43",
      "142"
    ]
  ],
  [
    "Ashibetsu",
    [
      "43.517",
      "142.183"
    ],
    "Hokkaido",
    [
      "43",
      "142"
    ]
  ],
  [
    "Ebetsu",
    [
      "43.100",
      "141.533"
    ],
    "Hokkaido",
    [
      "43",
      "142"
    ]
  ],
  [
    "Akabira",
    [
      "43.550",
      "142.050"
    ],
    "Hokkaido",
    [
      "43",
      "142"
    ]
  ],
  [
    "Monbetsu, Hokkaido",
    [
      "44.350",
      "143.350"
    ],
    "Hokkaido",
    [
      "43",
      "142"
    ]
  ],
  [
    "Mikasa, Hokkaido",
    [
      "43.250",
      "141.883"
    ],
    "Hokkaido",
    [
      "43",
      "142"
    ]
  ],
  [
    "Nemuro, Hokkaido",
    [
      "43.33000",
      "145.58278"
    ],
    "Hokkaido",
    [
      "43",
      "142"
    ]
  ],
  [
    "Chitose, Hokkaido",
    [
      "42.817",
      "141.650"
    ],
    "Hokkaido",
    [
      "43",
      "142"
    ]
  ],
  [
    "Takikawa, Hokkaido",
    [
      "43.550",
      "141.917"
    ],
    "Hokkaido",
    [
      "43",
      "142"
    ]
  ],
  [
    "Sunagawa, Hokkaido",
    [
      "43.500",
      "141.900"
    ],
    "Hokkaido",
    [
      "43",
      "142"
    ]
  ],
  [
    "Utashinai",
    [
      "43.517",
      "142.033"
    ],
    "Hokkaido",
    [
      "43",
      "142"
    ]
  ],
  [
    "Fukagawa, Hokkaido",
    [
      "43.71778",
      "142.04028"
    ],
    "Hokkaido",
    [
      "43",
      "142"
    ]
  ],
  [
    "Furano, Hokkaido",
    [
      "43.350",
      "142.383"
    ],
    "Hokkaido",
    [
      "43",
      "142"
    ]
  ],
  [
    "Noboribetsu",
    [
      "42.417",
      "141.100"
    ],
    "Hokkaido",
    [
      "43",
      "142"
    ]
  ],
  [
    "Eniwa, Hokkaido",
    [
      "42.883",
      "141.583"
    ],
    "Hokkaido",
    [
      "43",
      "142"
    ]
  ],
  [
    "Date, Hokkaido",
    [
      "42.467",
      "140.867"
    ],
    "Hokkaido",
    [
      "43",
      "142"
    ]
  ],
  [
    "Kitahiroshima, Hokkaido",
    [
      "42.983",
      "141.567"
    ],
    "Hokkaido",
    [
      "43",
      "142"
    ]
  ],
  [
    "Ishikari, Hokkaido",
    [
      "43.167",
      "141.317"
    ],
    "Hokkaido",
    [
      "43",
      "142"
    ]
  ],
  [
    "Shibetsu, Hokkaido",
    [
      "43.550",
      "141.917"
    ],
    "Hokkaido",
    [
      "43",
      "142"
    ]
  ],
  [
    "Kushiro",
    [
      "42.983",
      "144.383"
    ],
    "Hokkaido",
    [
      "43",
      "142"
    ]
  ],
  [
    "Hokuto, Hokkaido",
    [
      "41.82417",
      "140.65278"
    ],
    "Hokkaido",
    [
      "43",
      "142"
    ]
  ],
  [
    "Kitami",
    [
      "43.800",
      "143.900"
    ],
    "Hokkaido",
    [
      "43",
      "142"
    ]
  ],
  [
    "Nayoro",
    [
      "44.35583",
      "142.46333"
    ],
    "Hokkaido",
    [
      "43",
      "142"
    ]
  ],
  [
    "Kobe",
    [
      "34.69000",
      "135.19556"
    ],
    "Hy\u014dgo Prefecture"
  ],
  [
    "Himeji, Hy\u014dgo",
    [
      "34.817",
      "134.683"
    ],
    "Hy\u014dgo Prefecture"
  ],
  [
    "Amagasaki, Hy\u014dgo",
    [
      "34.733",
      "135.400"
    ],
    "Hy\u014dgo Prefecture"
  ],
  [
    "Akashi, Hy\u014dgo",
    [
      "34.650",
      "135.000"
    ],
    "Hy\u014dgo Prefecture"
  ],
  [
    "Nishinomiya, Hy\u014dgo",
    [
      "34.7375972",
      "135.3415639"
    ],
    "Hy\u014dgo Prefecture"
  ],
  [
    "Ashiya, Hy\u014dgo",
    [
      "34.72778",
      "135.30333"
    ],
    "Hy\u014dgo Prefecture"
  ],
  [
    "Itami, Hy\u014dgo",
    [
      "34.783",
      "135.400"
    ],
    "Hy\u014dgo Prefecture"
  ],
  [
    "Aioi, Hy\u014dgo",
    [
      "34.800",
      "134.467"
    ],
    "Hy\u014dgo Prefecture"
  ],
  [
    "Toyooka, Hy\u014dgo",
    [
      "35.550",
      "134.817"
    ],
    "Hy\u014dgo Prefecture"
  ],
  [
    "Kakogawa, Hy\u014dgo",
    [
      "34.750",
      "134.833"
    ],
    "Hy\u014dgo Prefecture"
  ],
  [
    "Ak\u014d, Hy\u014dgo",
    [
      "34.75167",
      "134.39306"
    ],
    "Hy\u014dgo Prefecture"
  ],
  [
    "Takarazuka, Hy\u014dgo",
    [
      "34.81139",
      "135.34056"
    ],
    "Hy\u014dgo Prefecture"
  ],
  [
    "Miki, Hy\u014dgo",
    [
      "34.79361",
      "134.99306"
    ],
    "Hy\u014dgo Prefecture"
  ],
  [
    "Takasago, Hy\u014dgo",
    [
      "34.767",
      "134.783"
    ],
    "Hy\u014dgo Prefecture"
  ],
  [
    "Kawanishi, Hy\u014dgo",
    [
      "34.833",
      "135.417"
    ],
    "Hy\u014dgo Prefecture"
  ],
  [
    "Ono, Hy\u014dgo",
    [
      "34.84972",
      "134.93417"
    ],
    "Hy\u014dgo Prefecture"
  ],
  [
    "Sanda, Hy\u014dgo",
    [
      "34.883",
      "135.233"
    ],
    "Hy\u014dgo Prefecture"
  ],
  [
    "Kasai, Hy\u014dgo",
    [
      "34.933",
      "134.833"
    ],
    "Hy\u014dgo Prefecture"
  ],
  [
    "Tamba-Sasayama, Hy\u014dgo",
    [
      "35.07250",
      "135.22194"
    ],
    "Hy\u014dgo Prefecture"
  ],
  [
    "Yabu, Hy\u014dgo",
    [
      "35.400",
      "134.767"
    ],
    "Hy\u014dgo Prefecture"
  ],
  [
    "Tamba, Hy\u014dgo",
    [
      "35.183",
      "135.033"
    ],
    "Hy\u014dgo Prefecture"
  ],
  [
    "Minamiawaji, Hy\u014dgo",
    [
      "34.300",
      "134.783"
    ],
    "Hy\u014dgo Prefecture"
  ],
  [
    "Asago, Hy\u014dgo",
    [
      "35.333",
      "134.850"
    ],
    "Hy\u014dgo Prefecture"
  ],
  [
    "Awaji, Hy\u014dgo",
    [
      "34.433",
      "134.917"
    ],
    "Hy\u014dgo Prefecture"
  ],
  [
    "Shis\u014d, Hy\u014dgo",
    [
      "35.000",
      "134.550"
    ],
    "Hy\u014dgo Prefecture"
  ],
  [
    "Nishiwaki, Hy\u014dgo",
    [
      "34.99028",
      "134.97222"
    ],
    "Hy\u014dgo Prefecture"
  ],
  [
    "Tatsuno, Hy\u014dgo",
    [
      "34.85083",
      "134.54528"
    ],
    "Hy\u014dgo Prefecture"
  ],
  [
    "Sumoto, Hy\u014dgo",
    [
      "34.350",
      "134.900"
    ],
    "Hy\u014dgo Prefecture"
  ],
  [
    "Kat\u014d, Hy\u014dgo",
    [
      "34.917",
      "134.967"
    ],
    "Hy\u014dgo Prefecture"
  ],
  [
    "Mito, Ibaraki",
    [
      "36.36583",
      "140.471250"
    ],
    "Ibaraki Prefecture"
  ],
  [
    "Hitachi, Ibaraki",
    [
      "36.599139",
      "140.651500"
    ],
    "Ibaraki Prefecture"
  ],
  [
    "Tsuchiura, Ibaraki",
    [
      "36.067",
      "140.200"
    ],
    "Ibaraki Prefecture"
  ],
  [
    "Y\u016bki, Ibaraki",
    [
      "36.305472",
      "139.876639"
    ],
    "Ibaraki Prefecture"
  ],
  [
    "Ry\u016bgasaki, Ibaraki",
    [
      "35.911556",
      "140.182306"
    ],
    "Ibaraki Prefecture"
  ],
  [
    "Shimotsuma, Ibaraki",
    [
      "36.184417",
      "139.967472"
    ],
    "Ibaraki Prefecture"
  ],
  [
    "J\u014ds\u014d, Ibaraki",
    [
      "36.023556",
      "139.993833"
    ],
    "Ibaraki Prefecture"
  ],
  [
    "Hitachi\u014dta, Ibaraki",
    [
      "36.538278",
      "140.530917"
    ],
    "Ibaraki Prefecture"
  ],
  [
    "Takahagi, Ibaraki",
    [
      "36.71917",
      "140.716722"
    ],
    "Ibaraki Prefecture"
  ],
  [
    "Kitaibaraki, Ibaraki",
    [
      "36.801889",
      "140.751028"
    ],
    "Ibaraki Prefecture"
  ],
  [
    "Toride, Ibaraki",
    [
      "35.911500",
      "140.050361"
    ],
    "Ibaraki Prefecture"
  ],
  [
    "Ushiku, Ibaraki",
    [
      "35.979361",
      "140.149556"
    ],
    "Ibaraki Prefecture"
  ],
  [
    "Tsukuba, Ibaraki",
    [
      "36.083472",
      "140.076444"
    ],
    "Ibaraki Prefecture"
  ],
  [
    "Hitachinaka, Ibaraki",
    [
      "36.396694",
      "140.534667"
    ],
    "Ibaraki Prefecture"
  ],
  [
    "Kashima, Ibaraki",
    [
      "35.965639",
      "140.644833"
    ],
    "Ibaraki Prefecture"
  ],
  [
    "Itako, Ibaraki",
    [
      "35.947139",
      "140.555361"
    ],
    "Ibaraki Prefecture"
  ],
  [
    "Moriya, Ibaraki",
    [
      "35.951417",
      "139.975417"
    ],
    "Ibaraki Prefecture"
  ],
  [
    "Hitachi\u014dmiya, Ibaraki",
    [
      "36.542528",
      "140.410889"
    ],
    "Ibaraki Prefecture"
  ],
  [
    "Naka, Ibaraki",
    [
      "36.457389",
      "140.486750"
    ],
    "Ibaraki Prefecture"
  ],
  [
    "Band\u014d, Ibaraki",
    [
      "36.048417",
      "139.888722"
    ],
    "Ibaraki Prefecture"
  ],
  [
    "Inashiki, Ibaraki",
    [
      "35.9565333",
      "140.323944"
    ],
    "Ibaraki Prefecture"
  ],
  [
    "Chikusei, Ibaraki",
    [
      "36.307083",
      "139.983139"
    ],
    "Ibaraki Prefecture"
  ],
  [
    "Kasumigaura, Ibaraki",
    [
      "36.151750",
      "140.237111"
    ],
    "Ibaraki Prefecture"
  ],
  [
    "Kamisu, Ibaraki",
    [
      "35.889944",
      "140.664528"
    ],
    "Ibaraki Prefecture"
  ],
  [
    "Namegata, Ibaraki",
    [
      "35.990500",
      "140.489028"
    ],
    "Ibaraki Prefecture"
  ],
  [
    "Koga, Ibaraki",
    [
      "36.178250",
      "139.755444"
    ],
    "Ibaraki Prefecture"
  ],
  [
    "Ishioka, Ibaraki",
    [
      "36.19083",
      "140.28722"
    ],
    "Ibaraki Prefecture"
  ],
  [
    "Sakuragawa, Ibaraki",
    [
      "36.327306",
      "140.09056"
    ],
    "Ibaraki Prefecture"
  ],
  [
    "Hokota, Ibaraki",
    [
      "36.158667",
      "140.516417"
    ],
    "Ibaraki Prefecture"
  ],
  [
    "Kasama, Ibaraki",
    [
      "36.345167",
      "140.304306"
    ],
    "Ibaraki Prefecture"
  ],
  [
    "Tsukubamirai, Ibaraki",
    [
      "35.96306",
      "140.037028"
    ],
    "Ibaraki Prefecture"
  ],
  [
    "Omitama, Ibaraki",
    [
      "36.239278",
      "140.352556"
    ],
    "Ibaraki Prefecture"
  ],
  [
    "Kanazawa, Ishikawa",
    [
      "36.561056",
      "136.656417"
    ],
    "Ishikawa Prefecture"
  ],
  [
    "Nonoichi, Ishikawa",
    [
      "36.519417",
      "136.609778"
    ],
    "Ishikawa Prefecture"
  ],
  [
    "Nanao, Ishikawa",
    [
      "37.043139",
      "136.967444"
    ],
    "Ishikawa Prefecture"
  ],
  [
    "Komatsu, Ishikawa",
    [
      "36.40833",
      "136.445528"
    ],
    "Ishikawa Prefecture"
  ],
  [
    "Suzu, Ishikawa",
    [
      "37.436333",
      "137.260472"
    ],
    "Ishikawa Prefecture"
  ],
  [
    "Hakui, Ishikawa",
    [
      "36.89361",
      "136.778972"
    ],
    "Ishikawa Prefecture"
  ],
  [
    "Kahoku, Ishikawa",
    [
      "36.719806",
      "136.706694"
    ],
    "Ishikawa Prefecture"
  ],
  [
    "Hakusan, Ishikawa",
    [
      "36.516639",
      "136.565583"
    ],
    "Ishikawa Prefecture"
  ],
  [
    "Nomi, Ishikawa",
    [
      "36.447000",
      "136.554083"
    ],
    "Ishikawa Prefecture"
  ],
  [
    "Kaga, Ishikawa",
    [
      "36.30278",
      "136.315028"
    ],
    "Ishikawa Prefecture"
  ],
  [
    "Wajima, Ishikawa",
    [
      "37.39056",
      "136.89917"
    ],
    "Ishikawa Prefecture"
  ],
  [
    "Morioka, Iwate",
    [
      "39.702083",
      "141.154500"
    ],
    "Iwate Prefecture"
  ],
  [
    "Kamaishi, Iwate",
    [
      "39.275806",
      "141.885694"
    ],
    "Iwate Prefecture"
  ],
  [
    "\u014cfunato, Iwate",
    [
      "39.068000",
      "141.725222"
    ],
    "Iwate Prefecture"
  ],
  [
    "Rikuzentakata, Iwate",
    [
      "39.028028",
      "141.625417"
    ],
    "Iwate Prefecture"
  ],
  [
    "Kitakami, Iwate",
    [
      "39.286750",
      "141.113222"
    ],
    "Iwate Prefecture"
  ],
  [
    "Miyako, Iwate",
    [
      "39.641417",
      "141.957139"
    ],
    "Iwate Prefecture"
  ],
  [
    "Hachimantai, Iwate",
    [
      "39.95611",
      "141.07111"
    ],
    "Iwate Prefecture"
  ],
  [
    "Ichinoseki, Iwate",
    [
      "38.93472",
      "141.126583"
    ],
    "Iwate Prefecture"
  ],
  [
    "T\u014dno, Iwate",
    [
      "39.327889",
      "141.533361"
    ],
    "Iwate Prefecture"
  ],
  [
    "Hanamaki, Iwate",
    [
      "39.38861",
      "141.116917"
    ],
    "Iwate Prefecture"
  ],
  [
    "Ninohe, Iwate",
    [
      "40.271250",
      "141.304778"
    ],
    "Iwate Prefecture"
  ],
  [
    "\u014csh\u016b, Iwate",
    [
      "39.144472",
      "141.139139"
    ],
    "Iwate Prefecture"
  ],
  [
    "Kuji, Iwate",
    [
      "40.190472",
      "141.775667"
    ],
    "Iwate Prefecture"
  ],
  [
    "Takizawa, Iwate",
    [
      "39.734694",
      "141.077056"
    ],
    "Iwate Prefecture"
  ],
  [
    "Takamatsu",
    [
      "34.350",
      "134.050"
    ],
    "Kagawa Prefecture"
  ],
  [
    "Marugame, Kagawa",
    [
      "34.283",
      "133.800"
    ],
    "Kagawa Prefecture"
  ],
  [
    "Sakaide, Kagawa",
    [
      "34.317",
      "133.867"
    ],
    "Kagawa Prefecture"
  ],
  [
    "Zents\u016bji, Kagawa",
    [
      "34.217",
      "133.783"
    ],
    "Kagawa Prefecture"
  ],
  [
    "Sanuki, Kagawa",
    [
      "34.32000",
      "134.17944"
    ],
    "Kagawa Prefecture"
  ],
  [
    "Higashikagawa, Kagawa",
    [
      "34.250",
      "134.367"
    ],
    "Kagawa Prefecture"
  ],
  [
    "Kan'onji, Kagawa",
    [
      "34.12722",
      "133.66139"
    ],
    "Kagawa Prefecture"
  ],
  [
    "Mitoyo, Kagawa",
    [
      "34.18250",
      "133.71500"
    ],
    "Kagawa Prefecture"
  ],
  [
    "Kagoshima, Kagoshima",
    [
      "31.600",
      "130.550"
    ],
    "Kagoshima Prefecture"
  ],
  [
    "Kanoya, Kagoshima",
    [
      "31.38306",
      "130.85194"
    ],
    "Kagoshima Prefecture"
  ],
  [
    "Makurazaki, Kagoshima",
    [
      "31.27278",
      "130.29694"
    ],
    "Kagoshima Prefecture"
  ],
  [
    "Akune, Kagoshima",
    [
      "32.017",
      "130.217"
    ],
    "Kagoshima Prefecture"
  ],
  [
    "Izumi, Kagoshima",
    [
      "32.083",
      "130.350"
    ],
    "Kagoshima Prefecture"
  ],
  [
    "Ibusuki, Kagoshima",
    [
      "31.25278",
      "130.63306"
    ],
    "Kagoshima Prefecture"
  ],
  [
    "Minamisatsuma, Kagoshima",
    [
      "31.41694",
      "130.32278"
    ],
    "Kagoshima Prefecture"
  ],
  [
    "Nishinoomote, Kagoshima",
    [
      "30.73222",
      "130.99667"
    ],
    "Kagoshima Prefecture"
  ],
  [
    "Tarumizu, Kagoshima",
    [
      "31.52278",
      "130.75944"
    ],
    "Kagoshima Prefecture"
  ],
  [
    "Satsumasendai, Kagoshima",
    [
      "31.817",
      "130.300"
    ],
    "Kagoshima Prefecture"
  ],
  [
    "Hioki, Kagoshima",
    [
      "31.61167",
      "130.37306"
    ],
    "Kagoshima Prefecture"
  ],
  [
    "Soo, Kagoshima",
    [
      "31.65333",
      "131.01917"
    ],
    "Kagoshima Prefecture"
  ],
  [
    "Ichikikushikino, Kagoshima",
    [
      "31.717",
      "130.267"
    ],
    "Kagoshima Prefecture"
  ],
  [
    "Kirishima, Kagoshima",
    [
      "31.74056",
      "130.76306"
    ],
    "Kagoshima Prefecture"
  ],
  [
    "Shibushi, Kagoshima",
    [
      "31.500",
      "131.050"
    ],
    "Kagoshima Prefecture"
  ],
  [
    "Amami, Kagoshima",
    [
      "28.37833",
      "129.49444"
    ],
    "Kagoshima Prefecture"
  ],
  [
    "Minamiky\u016bsh\u016b, Kagoshima",
    [
      "31.37778",
      "130.44194"
    ],
    "Kagoshima Prefecture"
  ],
  [
    "Isa, Kagoshima",
    [
      "32.05722",
      "130.61306"
    ],
    "Kagoshima Prefecture"
  ],
  [
    "Aira, Kagoshima",
    [
      "31.72833",
      "130.62778"
    ],
    "Kagoshima Prefecture"
  ],
  [
    "Yokohama",
    [
      "35.44417",
      "139.63806"
    ],
    "Kanagawa Prefecture"
  ],
  [
    "Yokosuka, Kanagawa",
    "Kanagawa Prefecture"
  ],
  [
    "Kawasaki, Kanagawa",
    [
      "35.517",
      "139.700"
    ],
    "Kanagawa Prefecture"
  ],
  [
    "Hiratsuka, Kanagawa",
    [
      "35.317",
      "139.350"
    ],
    "Kanagawa Prefecture"
  ],
  [
    "Kamakura, Kanagawa",
    [
      "35.31972",
      "139.55250"
    ],
    "Kanagawa Prefecture"
  ],
  [
    "Fujisawa, Kanagawa",
    [
      "35.350",
      "139.467"
    ],
    "Kanagawa Prefecture"
  ],
  [
    "Odawara, Kanagawa",
    [
      "35.250",
      "139.150"
    ],
    "Kanagawa Prefecture"
  ],
  [
    "Chigasaki, Kanagawa",
    [
      "35.333",
      "139.400"
    ],
    "Kanagawa Prefecture"
  ],
  [
    "Zushi, Kanagawa",
    [
      "35.283",
      "139.583"
    ],
    "Kanagawa Prefecture"
  ],
  [
    "Sagamihara",
    [
      "35.567",
      "139.367"
    ],
    "Kanagawa Prefecture"
  ],
  [
    "Miura, Kanagawa",
    [
      "35.150",
      "139.617"
    ],
    "Kanagawa Prefecture"
  ],
  [
    "Hadano, Kanagawa",
    [
      "35.367",
      "139.217"
    ],
    "Kanagawa Prefecture"
  ],
  [
    "Atsugi, Kanagawa",
    [
      "35.43333",
      "139.36667"
    ],
    "Kanagawa Prefecture"
  ],
  [
    "Yamato, Kanagawa",
    [
      "35.483",
      "139.450"
    ],
    "Kanagawa Prefecture"
  ],
  [
    "Isehara, Kanagawa",
    [
      "35.383",
      "139.300"
    ],
    "Kanagawa Prefecture"
  ],
  [
    "Ebina, Kanagawa",
    [
      "35.44639",
      "139.39083"
    ],
    "Kanagawa Prefecture"
  ],
  [
    "Zama, Kanagawa",
    [
      "35.483",
      "139.400"
    ],
    "Kanagawa Prefecture"
  ],
  [
    "Minamiashigara, Kanagawa",
    [
      "35.317",
      "139.100"
    ],
    "Kanagawa Prefecture"
  ],
  [
    "Ayase, Kanagawa",
    [
      "35.433",
      "139.433"
    ],
    "Kanagawa Prefecture"
  ],
  [
    "K\u014dchi, K\u014dchi",
    [
      "33.55889",
      "133.53139"
    ],
    "K\u014dchi Prefecture"
  ],
  [
    "Sukumo, K\u014dchi",
    [
      "32.933",
      "132.717"
    ],
    "K\u014dchi Prefecture"
  ],
  [
    "Aki, K\u014dchi",
    [
      "33.500",
      "133.900"
    ],
    "K\u014dchi Prefecture"
  ],
  [
    "Tosashimizu, K\u014dchi",
    [
      "32.783",
      "132.950"
    ],
    "K\u014dchi Prefecture"
  ],
  [
    "Susaki, K\u014dchi",
    [
      "33.39250",
      "133.29306"
    ],
    "K\u014dchi Prefecture"
  ],
  [
    "Tosa, K\u014dchi",
    [
      "33.500",
      "133.433"
    ],
    "K\u014dchi Prefecture"
  ],
  [
    "Muroto, K\u014dchi",
    [
      "33.29000",
      "134.15194"
    ],
    "K\u014dchi Prefecture"
  ],
  [
    "Nankoku, K\u014dchi",
    [
      "33.583",
      "133.633"
    ],
    "K\u014dchi Prefecture"
  ],
  [
    "Shimanto, K\u014dchi (city)",
    [
      "33.000",
      "132.933"
    ],
    "K\u014dchi Prefecture"
  ],
  [
    "Kami, K\u014dchi",
    [
      "33.600",
      "133.683"
    ],
    "K\u014dchi Prefecture"
  ],
  [
    "K\u014dnan, K\u014dchi",
    [
      "33.567",
      "133.700"
    ],
    "K\u014dchi Prefecture"
  ],
  [
    "Kumamoto",
    [
      "32.80306",
      "130.70778"
    ],
    "Kumamoto Prefecture"
  ],
  [
    "Yatsushiro, Kumamoto",
    [
      "32.500",
      "130.600"
    ],
    "Kumamoto Prefecture"
  ],
  [
    "Hitoyoshi, Kumamoto",
    [
      "32.217",
      "130.750"
    ],
    "Kumamoto Prefecture"
  ],
  [
    "Arao, Kumamoto",
    [
      "32.98333",
      "130.43528"
    ],
    "Kumamoto Prefecture"
  ],
  [
    "Minamata, Kumamoto",
    [
      "32.217",
      "130.400"
    ],
    "Kumamoto Prefecture"
  ],
  [
    "Tamana, Kumamoto",
    [
      "32.92806",
      "130.55944"
    ],
    "Kumamoto Prefecture"
  ],
  [
    "Yamaga, Kumamoto",
    [
      "33.01694",
      "130.68278"
    ],
    "Kumamoto Prefecture"
  ],
  [
    "Kikuchi, Kumamoto",
    [
      "32.983",
      "130.817"
    ],
    "Kumamoto Prefecture"
  ],
  [
    "Uto, Kumamoto",
    [
      "32.68278",
      "130.66694"
    ],
    "Kumamoto Prefecture"
  ],
  [
    "Kamiamakusa, Kumamoto",
    [
      "32.500",
      "130.417"
    ],
    "Kumamoto Prefecture"
  ],
  [
    "Uki, Kumamoto",
    [
      "32.64500",
      "130.68639"
    ],
    "Kumamoto Prefecture"
  ],
  [
    "Aso, Kumamoto",
    [
      "32.94833",
      "131.12389"
    ],
    "Kumamoto Prefecture"
  ],
  [
    "K\u014dshi, Kumamoto",
    [
      "32.883",
      "130.783"
    ],
    "Kumamoto Prefecture"
  ],
  [
    "Amakusa, Kumamoto",
    [
      "32.467",
      "130.200"
    ],
    "Kumamoto Prefecture"
  ],
  [
    "Kyoto",
    [
      "35.01167",
      "135.76833"
    ],
    "Kyoto Prefecture"
  ],
  [
    "Fukuchiyama, Kyoto",
    [
      "35.300",
      "135.133"
    ],
    "Kyoto Prefecture"
  ],
  [
    "Maizuru, Kyoto",
    [
      "35.467",
      "135.383"
    ],
    "Kyoto Prefecture"
  ],
  [
    "Ayabe, Kyoto",
    [
      "35.300",
      "135.267"
    ],
    "Kyoto Prefecture"
  ],
  [
    "Uji, Kyoto",
    [
      "34.88444",
      "135.79972"
    ],
    "Kyoto Prefecture"
  ],
  [
    "Miyazu, Kyoto",
    [
      "35.533",
      "135.200"
    ],
    "Kyoto Prefecture"
  ],
  [
    "Kameoka, Kyoto",
    [
      "35.017",
      "135.567"
    ],
    "Kyoto Prefecture"
  ],
  [
    "J\u014dy\u014d, Kyoto",
    [
      "34.85306",
      "135.78000"
    ],
    "Kyoto Prefecture"
  ],
  [
    "Muk\u014d, Kyoto",
    [
      "34.950",
      "135.700"
    ],
    "Kyoto Prefecture"
  ],
  [
    "Nagaokaky\u014d, Kyoto",
    [
      "34.933",
      "135.700"
    ],
    "Kyoto Prefecture"
  ],
  [
    "Yawata, Kyoto",
    [
      "34.867",
      "135.700"
    ],
    "Kyoto Prefecture"
  ],
  [
    "Ky\u014dtanabe, Kyoto",
    [
      "34.817",
      "135.767"
    ],
    "Kyoto Prefecture"
  ],
  [
    "Ky\u014dtango, Kyoto",
    [
      "35.62417",
      "135.06111"
    ],
    "Kyoto Prefecture"
  ],
  [
    "Nantan, Kyoto",
    [
      "35.100",
      "135.467"
    ],
    "Kyoto Prefecture"
  ],
  [
    "Kizugawa, Kyoto",
    [
      "34.733",
      "135.817"
    ],
    "Kyoto Prefecture"
  ],
  [
    "Yokkaichi, Mie",
    [
      "34.965028",
      "136.624417"
    ],
    "Mie Prefecture"
  ],
  [
    "Matsusaka, Mie",
    [
      "34.577944",
      "136.527583"
    ],
    "Mie Prefecture"
  ],
  [
    "Kuwana, Mie",
    [
      "35.067",
      "136.683"
    ],
    "Mie Prefecture"
  ],
  [
    "Suzuka, Mie",
    [
      "34.881972",
      "136.58417"
    ],
    "Mie Prefecture"
  ],
  [
    "Nabari, Mie",
    [
      "34.627583",
      "136.108389"
    ],
    "Mie Prefecture"
  ],
  [
    "Owase, Mie",
    [
      "34.070778",
      "136.190972"
    ],
    "Mie Prefecture"
  ],
  [
    "Kameyama, Mie",
    [
      "34.85583",
      "136.45167"
    ],
    "Mie Prefecture"
  ],
  [
    "Toba, Mie",
    [
      "34.481333",
      "136.843417"
    ],
    "Mie Prefecture"
  ],
  [
    "Inabe, Mie",
    [
      "35.11556",
      "136.56139"
    ],
    "Mie Prefecture"
  ],
  [
    "Shima, Mie",
    [
      "34.333",
      "136.833"
    ],
    "Mie Prefecture"
  ],
  [
    "Iga, Mie",
    [
      "34.767",
      "136.133"
    ],
    "Mie Prefecture"
  ],
  [
    "Ise, Mie",
    [
      "34.483",
      "136.717"
    ],
    "Mie Prefecture"
  ],
  [
    "Kumano, Mie",
    [
      "33.888639",
      "136.100222"
    ],
    "Mie Prefecture"
  ],
  [
    "Tsu, Mie",
    [
      "34.718444",
      "136.505722"
    ],
    "Mie Prefecture"
  ],
  [
    "Sendai",
    [
      "38.268222",
      "140.869417"
    ],
    "Miyagi Prefecture"
  ],
  [
    "Ishinomaki",
    [
      "38.417583",
      "141.302722"
    ],
    "Miyagi Prefecture"
  ],
  [
    "Shiogama",
    [
      "38.314361",
      "141.021972"
    ],
    "Miyagi Prefecture"
  ],
  [
    "Shiroishi, Miyagi",
    [
      "38.0024694",
      "140.6196694"
    ],
    "Miyagi Prefecture"
  ],
  [
    "Natori, Miyagi",
    [
      "38.171528",
      "140.891806"
    ],
    "Miyagi Prefecture"
  ],
  [
    "Kakuda, Miyagi",
    [
      "37.977028",
      "140.782056"
    ],
    "Miyagi Prefecture"
  ],
  [
    "Tagaj\u014d",
    [
      "38.293833",
      "141.004250"
    ],
    "Miyagi Prefecture"
  ],
  [
    "Iwanuma",
    [
      "38.104278",
      "140.870167"
    ],
    "Miyagi Prefecture"
  ],
  [
    "Tome, Miyagi",
    [
      "38.691833",
      "141.187750"
    ],
    "Miyagi Prefecture"
  ],
  [
    "Kurihara, Miyagi",
    [
      "38.730111",
      "141.021472"
    ],
    "Miyagi Prefecture"
  ],
  [
    "Higashimatsushima",
    [
      "38.426250",
      "141.210417"
    ],
    "Miyagi Prefecture"
  ],
  [
    "Kesennuma",
    [
      "38.90806",
      "141.569944"
    ],
    "Miyagi Prefecture"
  ],
  [
    "\u014csaki, Miyagi",
    [
      "38.577111",
      "140.955583"
    ],
    "Miyagi Prefecture"
  ],
  [
    "Tomiya, Miyagi",
    [
      "38.400",
      "140.883"
    ],
    "Miyagi Prefecture"
  ],
  [
    "Miyazaki (city)",
    [
      "31.917",
      "131.417"
    ],
    "Miyazaki Prefecture"
  ],
  [
    "Miyakonoj\u014d",
    [
      "31.717",
      "131.067"
    ],
    "Miyazaki Prefecture"
  ],
  [
    "Nobeoka",
    [
      "32.583",
      "131.667"
    ],
    "Miyazaki Prefecture"
  ],
  [
    "Nichinan, Miyazaki",
    [
      "31.60222",
      "131.38000"
    ],
    "Miyazaki Prefecture"
  ],
  [
    "Kobayashi, Miyazaki",
    [
      "31.99444",
      "130.95167"
    ],
    "Miyazaki Prefecture"
  ],
  [
    "Hy\u016bga, Miyazaki",
    [
      "32.417",
      "131.617"
    ],
    "Miyazaki Prefecture"
  ],
  [
    "Kushima, Miyazaki",
    [
      "31.46806",
      "131.24667"
    ],
    "Miyazaki Prefecture"
  ],
  [
    "Saito, Miyazaki",
    [
      "32.117",
      "131.400"
    ],
    "Miyazaki Prefecture"
  ],
  [
    "Ebino, Miyazaki",
    [
      "32.033",
      "130.817"
    ],
    "Miyazaki Prefecture"
  ],
  [
    "Matsumoto, Nagano",
    [
      "36.238000",
      "137.971972"
    ],
    "Nagano Prefecture"
  ],
  [
    "Okaya, Nagano",
    [
      "36.067111",
      "138.049306"
    ],
    "Nagano Prefecture"
  ],
  [
    "Suwa, Nagano",
    [
      "36.039139",
      "138.114028"
    ],
    "Nagano Prefecture"
  ],
  [
    "Suzaka, Nagano",
    [
      "36.65111",
      "138.307250"
    ],
    "Nagano Prefecture"
  ],
  [
    "Komoro, Nagano",
    [
      "36.327500",
      "138.425833"
    ],
    "Nagano Prefecture"
  ],
  [
    "Komagane, Nagano",
    [
      "35.728778",
      "137.933861"
    ],
    "Nagano Prefecture"
  ],
  [
    "\u014cmachi, Nagano",
    [
      "36.503000",
      "137.85111"
    ],
    "Nagano Prefecture"
  ],
  [
    "Iiyama, Nagano",
    [
      "36.851639",
      "138.365528"
    ],
    "Nagano Prefecture"
  ],
  [
    "Iida, Nagano",
    [
      "35.51500",
      "137.82139"
    ],
    "Nagano Prefecture"
  ],
  [
    "Chino, Nagano",
    [
      "35.995528",
      "138.158806"
    ],
    "Nagano Prefecture"
  ],
  [
    "Shiojiri, Nagano",
    [
      "36.114972",
      "137.953444"
    ],
    "Nagano Prefecture"
  ],
  [
    "Nagano, Nagano",
    [
      "36.64861",
      "138.19472"
    ],
    "Nagano Prefecture"
  ],
  [
    "Chikuma, Nagano",
    [
      "36.53389",
      "138.119972"
    ],
    "Nagano Prefecture"
  ],
  [
    "T\u014dmi, Nagano",
    [
      "36.359389",
      "138.330389"
    ],
    "Nagano Prefecture"
  ],
  [
    "Nakano, Nagano",
    [
      "36.742000",
      "138.369417"
    ],
    "Nagano Prefecture"
  ],
  [
    "Saku, Nagano",
    [
      "36.248806",
      "138.47694"
    ],
    "Nagano Prefecture"
  ],
  [
    "Azumino, Nagano",
    [
      "36.3039361",
      "137.9057806"
    ],
    "Nagano Prefecture"
  ],
  [
    "Ueda, Nagano",
    [
      "36.401889",
      "138.249083"
    ],
    "Nagano Prefecture"
  ],
  [
    "Ina, Nagano",
    [
      "35.827528",
      "137.953972"
    ],
    "Nagano Prefecture"
  ],
  [
    "Nagasaki, Nagasaki",
    [
      "32.74472",
      "129.87361"
    ],
    "Nagasaki Prefecture"
  ],
  [
    "Sasebo, Nagasaki",
    [
      "33.18000",
      "129.71500"
    ],
    "Nagasaki Prefecture"
  ],
  [
    "Shimabara, Nagasaki",
    [
      "32.78778",
      "130.36972"
    ],
    "Nagasaki Prefecture"
  ],
  [
    "\u014cmura, Nagasaki",
    [
      "32.90000",
      "129.95833"
    ],
    "Nagasaki Prefecture"
  ],
  [
    "Tsushima, Nagasaki",
    [
      "34.200",
      "129.283"
    ],
    "Nagasaki Prefecture"
  ],
  [
    "Iki, Nagasaki",
    [
      "33.74972",
      "129.69139"
    ],
    "Nagasaki Prefecture"
  ],
  [
    "Got\u014d, Nagasaki",
    [
      "32.700",
      "128.833"
    ],
    "Nagasaki Prefecture"
  ],
  [
    "Isahaya, Nagasaki",
    [
      "32.850",
      "130.067"
    ],
    "Nagasaki Prefecture"
  ],
  [
    "Saikai, Nagasaki",
    [
      "32.933",
      "129.650"
    ],
    "Nagasaki Prefecture"
  ],
  [
    "Hirado, Nagasaki",
    [
      "33.367",
      "129.550"
    ],
    "Nagasaki Prefecture"
  ],
  [
    "Unzen, Nagasaki",
    [
      "32.83528",
      "130.18750"
    ],
    "Nagasaki Prefecture"
  ],
  [
    "Matsuura, Nagasaki",
    [
      "33.333",
      "129.717"
    ],
    "Nagasaki Prefecture"
  ],
  [
    "Minamishimabara, Nagasaki",
    [
      "32.667",
      "130.300"
    ],
    "Nagasaki Prefecture"
  ],
  [
    "Nara, Nara",
    [
      "34.68444",
      "135.80500"
    ],
    "Nara Prefecture"
  ],
  [
    "Yamatotakada, Nara",
    [
      "34.517",
      "135.733"
    ],
    "Nara Prefecture"
  ],
  [
    "Yamatok\u014driyama, Nara",
    [
      "34.650",
      "135.783"
    ],
    "Nara Prefecture"
  ],
  [
    "Tenri, Nara",
    [
      "34.59667",
      "135.83722"
    ],
    "Nara Prefecture"
  ],
  [
    "Kashihara, Nara",
    [
      "34.517",
      "135.800"
    ],
    "Nara Prefecture"
  ],
  [
    "Sakurai, Nara",
    [
      "34.517",
      "135.850"
    ],
    "Nara Prefecture"
  ],
  [
    "Goj\u014d, Nara",
    [
      "34.34861",
      "135.69639"
    ],
    "Nara Prefecture"
  ],
  [
    "Gose, Nara",
    [
      "34.467",
      "135.733"
    ],
    "Nara Prefecture"
  ],
  [
    "Ikoma, Nara",
    [
      "34.700",
      "135.700"
    ],
    "Nara Prefecture"
  ],
  [
    "Kashiba, Nara",
    [
      "34.533",
      "135.700"
    ],
    "Nara Prefecture"
  ],
  [
    "Katsuragi, Nara",
    [
      "34.483",
      "135.733"
    ],
    "Nara Prefecture"
  ],
  [
    "Uda, Nara",
    [
      "34.517",
      "135.967"
    ],
    "Nara Prefecture"
  ],
  [
    "Niigata, Niigata",
    [
      "37.91611",
      "139.03639"
    ],
    "Niigata Prefecture"
  ],
  [
    "Nagaoka, Niigata",
    [
      "37.446194",
      "138.851250"
    ],
    "Niigata Prefecture"
  ],
  [
    "Kashiwazaki, Niigata",
    [
      "37.371917",
      "138.559000"
    ],
    "Niigata Prefecture"
  ],
  [
    "Shibata, Niigata",
    [
      "37.947917",
      "139.327278"
    ],
    "Niigata Prefecture"
  ],
  [
    "Ojiya, Niigata",
    [
      "37.314361",
      "138.795083"
    ],
    "Niigata Prefecture"
  ],
  [
    "Kamo, Niigata",
    [
      "37.666306",
      "139.040222"
    ],
    "Niigata Prefecture"
  ],
  [
    "Mitsuke, Niigata",
    [
      "37.531583",
      "138.912750"
    ],
    "Niigata Prefecture"
  ],
  [
    "Murakami, Niigata",
    [
      "38.224000",
      "139.48000"
    ],
    "Niigata Prefecture"
  ],
  [
    "My\u014dk\u014d, Niigata",
    [
      "37.025194",
      "138.253528"
    ],
    "Niigata Prefecture"
  ],
  [
    "J\u014detsu, Niigata",
    [
      "37.147861",
      "138.236083"
    ],
    "Niigata Prefecture"
  ],
  [
    "Sado, Niigata",
    [
      "38.01833",
      "138.36833"
    ],
    "Niigata Prefecture"
  ],
  [
    "Agano, Niigata",
    [
      "37.83444",
      "139.226000"
    ],
    "Niigata Prefecture"
  ],
  [
    "Uonuma, Niigata",
    [
      "37.230111",
      "138.961472"
    ],
    "Niigata Prefecture"
  ],
  [
    "Minamiuonuma, Niigata",
    [
      "37.065528",
      "138.876083"
    ],
    "Niigata Prefecture"
  ],
  [
    "Itoigawa, Niigata",
    [
      "37.039028",
      "137.862667"
    ],
    "Niigata Prefecture"
  ],
  [
    "T\u014dkamachi, Niigata",
    [
      "37.13333",
      "138.75000"
    ],
    "Niigata Prefecture"
  ],
  [
    "Sanj\u014d, Niigata",
    [
      "37.636778",
      "138.96167"
    ],
    "Niigata Prefecture"
  ],
  [
    "Tainai, Niigata",
    [
      "38.059694",
      "139.410333"
    ],
    "Niigata Prefecture"
  ],
  [
    "Gosen, Niigata",
    [
      "37.74444",
      "139.182611"
    ],
    "Niigata Prefecture"
  ],
  [
    "Tsubame, Niigata",
    [
      "37.673083",
      "138.88222"
    ],
    "Niigata Prefecture"
  ],
  [
    "\u014cita, \u014cita",
    [
      "33.23333",
      "131.60667"
    ],
    "\u014cita Prefecture"
  ],
  [
    "Beppu, \u014cita",
    [
      "33.279528",
      "131.500028"
    ],
    "\u014cita Prefecture"
  ],
  [
    "Nakatsu, \u014cita",
    [
      "33.59917",
      "131.19056"
    ],
    "\u014cita Prefecture"
  ],
  [
    "Hita, \u014cita",
    [
      "33.317",
      "130.933"
    ],
    "\u014cita Prefecture"
  ],
  [
    "Saiki, \u014cita",
    [
      "32.967",
      "131.900"
    ],
    "\u014cita Prefecture"
  ],
  [
    "Usuki, \u014cita",
    [
      "33.133",
      "131.800"
    ],
    "\u014cita Prefecture"
  ],
  [
    "Tsukumi, \u014cita",
    [
      "33.067",
      "131.867"
    ],
    "\u014cita Prefecture"
  ],
  [
    "Taketa, \u014cita",
    [
      "32.967",
      "131.400"
    ],
    "\u014cita Prefecture"
  ],
  [
    "Bungotakada, \u014cita",
    [
      "33.550",
      "131.450"
    ],
    "\u014cita Prefecture"
  ],
  [
    "Usa, \u014cita",
    [
      "33.5319719",
      "131.3495446"
    ],
    "\u014cita Prefecture"
  ],
  [
    "Bungo-\u014cno, \u014cita",
    [
      "32.983",
      "131.583"
    ],
    "\u014cita Prefecture"
  ],
  [
    "Kitsuki, \u014cita",
    [
      "33.417",
      "131.617"
    ],
    "\u014cita Prefecture"
  ],
  [
    "Yufu, \u014cita",
    [
      "33.183",
      "131.433"
    ],
    "\u014cita Prefecture"
  ],
  [
    "Kunisaki, \u014cita",
    [
      "33.56528",
      "131.73111"
    ],
    "\u014cita Prefecture"
  ],
  [
    "Okayama",
    [
      "34.650",
      "133.917"
    ],
    "Okayama Prefecture"
  ],
  [
    "Kurashiki, Okayama",
    [
      "34.58500",
      "133.77222"
    ],
    "Okayama Prefecture"
  ],
  [
    "Tsuyama, Okayama",
    [
      "35.06917",
      "134.00444"
    ],
    "Okayama Prefecture"
  ],
  [
    "Tamano, Okayama",
    [
      "34.48861",
      "133.94861"
    ],
    "Okayama Prefecture"
  ],
  [
    "Kasaoka, Okayama",
    [
      "34.50389",
      "133.51000"
    ],
    "Okayama Prefecture"
  ],
  [
    "Ibara, Okayama",
    [
      "34.600",
      "133.467"
    ],
    "Okayama Prefecture"
  ],
  [
    "S\u014dja, Okayama",
    [
      "34.67278",
      "133.74639"
    ],
    "Okayama Prefecture"
  ],
  [
    "Takahashi, Okayama",
    [
      "34.79139",
      "133.61639"
    ],
    "Okayama Prefecture"
  ],
  [
    "Niimi, Okayama",
    [
      "34.97389",
      "133.47306"
    ],
    "Okayama Prefecture"
  ],
  [
    "Bizen, Okayama",
    [
      "34.74528",
      "134.18889"
    ],
    "Okayama Prefecture"
  ],
  [
    "Setouchi, Okayama",
    [
      "34.667",
      "134.100"
    ],
    "Okayama Prefecture"
  ],
  [
    "Akaiwa, Okayama",
    [
      "34.75528",
      "134.01889"
    ],
    "Okayama Prefecture"
  ],
  [
    "Maniwa, Okayama",
    [
      "35.07583",
      "133.75250"
    ],
    "Okayama Prefecture"
  ],
  [
    "Mimasaka, Okayama",
    [
      "35.00861",
      "134.14861"
    ],
    "Okayama Prefecture"
  ],
  [
    "Asakuchi, Okayama",
    [
      "34.52472",
      "133.58750"
    ],
    "Okayama Prefecture"
  ],
  [
    "Naha, Okinawa",
    [
      "26.21222",
      "127.67917"
    ],
    "Okinawa Prefecture"
  ],
  [
    "Ishigaki, Okinawa",
    [
      "24.34056",
      "124.15556"
    ],
    "Okinawa Prefecture"
  ],
  [
    "Ginowan, Okinawa",
    [
      "26.28167",
      "127.77833"
    ],
    "Okinawa Prefecture"
  ],
  [
    "Urasoe, Okinawa",
    [
      "26.24583",
      "127.72194"
    ],
    "Okinawa Prefecture"
  ],
  [
    "Nago, Okinawa",
    [
      "26.59167",
      "127.97750"
    ],
    "Okinawa Prefecture"
  ],
  [
    "Itoman, Okinawa",
    [
      "26.12361",
      "127.66583"
    ],
    "Okinawa Prefecture"
  ],
  [
    "Okinawa, Okinawa",
    [
      "26.33417",
      "127.80556"
    ],
    "Okinawa Prefecture"
  ],
  [
    "Tomigusuku, Okinawa",
    [
      "26.16111",
      "127.66889"
    ],
    "Okinawa Prefecture"
  ],
  [
    "Uruma, Okinawa",
    [
      "26.37917",
      "127.85750"
    ],
    "Okinawa Prefecture"
  ],
  [
    "Miyakojima, Okinawa",
    [
      "24.80556",
      "125.28111"
    ],
    "Okinawa Prefecture"
  ],
  [
    "Nanj\u014d, Okinawa",
    [
      "26.16306",
      "127.77056"
    ],
    "Okinawa Prefecture"
  ],
  [
    "Osaka",
    [
      "34.69389",
      "135.50222"
    ],
    "Osaka Prefecture"
  ],
  [
    "Sakai",
    [
      "34.57333",
      "135.48306"
    ],
    "Osaka Prefecture"
  ],
  [
    "Kishiwada, Osaka",
    [
      "34.467",
      "135.367"
    ],
    "Osaka Prefecture"
  ],
  [
    "Toyonaka, Osaka",
    [
      "34.783",
      "135.467"
    ],
    "Osaka Prefecture"
  ],
  [
    "Ikeda, Osaka",
    [
      "34.82167",
      "135.42861"
    ],
    "Osaka Prefecture"
  ],
  [
    "Suita, Osaka",
    [
      "34.75944",
      "135.51694"
    ],
    "Osaka Prefecture"
  ],
  [
    "Izumi\u014dtsu, Osaka",
    [
      "34.500",
      "135.400"
    ],
    "Osaka Prefecture"
  ],
  [
    "Takatsuki, Osaka",
    [
      "34.84611",
      "135.61750"
    ],
    "Osaka Prefecture"
  ],
  [
    "Kaizuka, Osaka",
    [
      "34.433",
      "135.367"
    ],
    "Osaka Prefecture"
  ],
  [
    "Moriguchi, Osaka",
    [
      "34.73750",
      "135.56417"
    ],
    "Osaka Prefecture"
  ],
  [
    "Hirakata, Osaka",
    [
      "34.817",
      "135.650"
    ],
    "Osaka Prefecture"
  ],
  [
    "Ibaraki, Osaka",
    [
      "34.81639",
      "135.56861"
    ],
    "Osaka Prefecture"
  ],
  [
    "Yao, Osaka",
    [
      "34.6268694",
      "135.6009861"
    ],
    "Osaka Prefecture"
  ],
  [
    "Izumisano, Osaka",
    [
      "34.400",
      "135.333"
    ],
    "Osaka Prefecture"
  ],
  [
    "Tondabayashi, Osaka",
    [
      "34.500",
      "135.600"
    ],
    "Osaka Prefecture"
  ],
  [
    "Neyagawa, Osaka",
    [
      "34.767",
      "135.633"
    ],
    "Osaka Prefecture"
  ],
  [
    "Kawachinagano, Osaka",
    [
      "34.467",
      "135.567"
    ],
    "Osaka Prefecture"
  ],
  [
    "Matsubara, Osaka",
    [
      "34.583",
      "135.550"
    ],
    "Osaka Prefecture"
  ],
  [
    "Dait\u014d, Osaka",
    [
      "34.717",
      "135.617"
    ],
    "Osaka Prefecture"
  ],
  [
    "Izumi, Osaka",
    [
      "34.483",
      "135.417"
    ],
    "Osaka Prefecture"
  ],
  [
    "Minoh, Osaka",
    [
      "34.82694",
      "135.47056"
    ],
    "Osaka Prefecture"
  ],
  [
    "Kashiwara, Osaka",
    [
      "34.583",
      "135.633"
    ],
    "Osaka Prefecture"
  ],
  [
    "Habikino, Osaka",
    [
      "34.550",
      "135.600"
    ],
    "Osaka Prefecture"
  ],
  [
    "Kadoma, Osaka",
    [
      "34.733",
      "135.583"
    ],
    "Osaka Prefecture"
  ],
  [
    "Settsu, Osaka",
    [
      "34.77722",
      "135.56222"
    ],
    "Osaka Prefecture"
  ],
  [
    "Takaishi, Osaka",
    [
      "34.517",
      "135.450"
    ],
    "Osaka Prefecture"
  ],
  [
    "Fujiidera, Osaka",
    [
      "34.567",
      "135.600"
    ],
    "Osaka Prefecture"
  ],
  [
    "Higashi\u014dsaka, Osaka",
    [
      "34.67944",
      "135.60083"
    ],
    "Osaka Prefecture"
  ],
  [
    "Sennan, Osaka",
    [
      "34.36278",
      "135.27611"
    ],
    "Osaka Prefecture"
  ],
  [
    "Shij\u014dnawate, Osaka",
    [
      "34.74000",
      "135.63944"
    ],
    "Osaka Prefecture"
  ],
  [
    "Katano, Osaka",
    [
      "34.783",
      "135.683"
    ],
    "Osaka Prefecture"
  ],
  [
    "\u014csakasayama, Osaka",
    [
      "34.500",
      "135.550"
    ],
    "Osaka Prefecture"
  ],
  [
    "Hannan, Osaka",
    [
      "34.35972",
      "135.23944"
    ],
    "Osaka Prefecture"
  ],
  [
    "Tosu, Saga",
    [
      "33.383",
      "130.500"
    ],
    "Saga Prefecture"
  ],
  [
    "Imari, Saga",
    [
      "33.267",
      "129.883"
    ],
    "Saga Prefecture"
  ],
  [
    "Kashima, Saga",
    [
      "33.10361",
      "130.09889"
    ],
    "Saga Prefecture"
  ],
  [
    "Taku, Saga",
    [
      "33.283",
      "130.117"
    ],
    "Saga Prefecture"
  ],
  [
    "Karatsu, Saga",
    [
      "33.450",
      "129.967"
    ],
    "Saga Prefecture"
  ],
  [
    "Ogi, Saga",
    [
      "33.250",
      "130.200"
    ],
    "Saga Prefecture"
  ],
  [
    "Saga, Saga",
    [
      "33.26667",
      "130.30000"
    ],
    "Saga Prefecture"
  ],
  [
    "Ureshino, Saga",
    [
      "33.133",
      "130.067"
    ],
    "Saga Prefecture"
  ],
  [
    "Takeo, Saga",
    [
      "33.200",
      "130.017"
    ],
    "Saga Prefecture"
  ],
  [
    "Kanzaki, Saga",
    [
      "33.317",
      "130.367"
    ],
    "Saga Prefecture"
  ],
  [
    "Kawagoe, Saitama",
    [
      "35.925139",
      "139.485778"
    ],
    "Saitama Prefecture"
  ],
  [
    "Kawaguchi, Saitama",
    [
      "35.807694",
      "139.724111"
    ],
    "Saitama Prefecture"
  ],
  [
    "Gy\u014dda, Saitama",
    [
      "36.13889",
      "139.455639"
    ],
    "Saitama Prefecture"
  ],
  [
    "Chichibu, Saitama",
    [
      "35.991778",
      "139.085472"
    ],
    "Saitama Prefecture"
  ],
  [
    "Tokorozawa, Saitama",
    [
      "35.799611",
      "139.46861"
    ],
    "Saitama Prefecture"
  ],
  [
    "Hann\u014d, Saitama",
    [
      "35.855667",
      "139.327722"
    ],
    "Saitama Prefecture"
  ],
  [
    "Kazo, Saitama",
    [
      "36.131444",
      "139.601778"
    ],
    "Saitama Prefecture"
  ],
  [
    "Higashimatsuyama, Saitama",
    [
      "36.042167",
      "139.399917"
    ],
    "Saitama Prefecture"
  ],
  [
    "Sayama, Saitama",
    [
      "35.852972",
      "139.412194"
    ],
    "Saitama Prefecture"
  ],
  [
    "Hany\u016b, Saitama",
    [
      "36.172639",
      "139.548472"
    ],
    "Saitama Prefecture"
  ],
  [
    "K\u014dnosu, Saitama",
    [
      "36.065889",
      "139.522194"
    ],
    "Saitama Prefecture"
  ],
  [
    "Ageo, Saitama",
    [
      "35.977389",
      "139.593194"
    ],
    "Saitama Prefecture"
  ],
  [
    "S\u014dka, Saitama",
    [
      "35.825389",
      "139.805333"
    ],
    "Saitama Prefecture"
  ],
  [
    "Koshigaya, Saitama",
    [
      "35.891139",
      "139.790917"
    ],
    "Saitama Prefecture"
  ],
  [
    "Warabi, Saitama",
    [
      "35.825583",
      "139.67972"
    ],
    "Saitama Prefecture"
  ],
  [
    "Toda, Saitama",
    [
      "35.817611",
      "139.677917"
    ],
    "Saitama Prefecture"
  ],
  [
    "Iruma, Saitama",
    [
      "35.835806",
      "139.391139"
    ],
    "Saitama Prefecture"
  ],
  [
    "Asaka, Saitama",
    [
      "35.797194",
      "139.59389"
    ],
    "Saitama Prefecture"
  ],
  [
    "Shiki, Saitama",
    [
      "35.83667",
      "139.580306"
    ],
    "Saitama Prefecture"
  ],
  [
    "Wak\u014d, Saitama",
    [
      "35.781222",
      "139.605694"
    ],
    "Saitama Prefecture"
  ],
  [
    "Niiza, Saitama",
    [
      "35.793500",
      "139.565306"
    ],
    "Saitama Prefecture"
  ],
  [
    "Okegawa, Saitama",
    [
      "36.005722",
      "139.542694"
    ],
    "Saitama Prefecture"
  ],
  [
    "Kuki, Saitama",
    [
      "36.062083",
      "139.666806"
    ],
    "Saitama Prefecture"
  ],
  [
    "Kitamoto, Saitama",
    [
      "36.026889",
      "139.530194"
    ],
    "Saitama Prefecture"
  ],
  [
    "Yashio, Saitama",
    [
      "35.822528",
      "139.839222"
    ],
    "Saitama Prefecture"
  ],
  [
    "Fujimi, Saitama",
    [
      "35.856556",
      "139.54917"
    ],
    "Saitama Prefecture"
  ],
  [
    "Misato, Saitama (city)",
    [
      "35.830139",
      "139.872333"
    ],
    "Saitama Prefecture"
  ],
  [
    "Hasuda, Saitama",
    [
      "35.994500",
      "139.662389"
    ],
    "Saitama Prefecture"
  ],
  [
    "Sakado, Saitama",
    [
      "35.957250",
      "139.403028"
    ],
    "Saitama Prefecture"
  ],
  [
    "Satte, Saitama",
    [
      "36.078083",
      "139.725861"
    ],
    "Saitama Prefecture"
  ],
  [
    "Tsurugashima, Saitama",
    [
      "35.934500",
      "139.393083"
    ],
    "Saitama Prefecture"
  ],
  [
    "Hidaka, Saitama",
    [
      "35.907806",
      "139.339083"
    ],
    "Saitama Prefecture"
  ],
  [
    "Yoshikawa, Saitama",
    [
      "35.893861",
      "139.841417"
    ],
    "Saitama Prefecture"
  ],
  [
    "Saitama, Saitama",
    [
      "35.86139",
      "139.64556"
    ],
    "Saitama Prefecture"
  ],
  [
    "Kumagaya, Saitama",
    [
      "36.147389",
      "139.388639"
    ],
    "Saitama Prefecture"
  ],
  [
    "Kasukabe, Saitama",
    [
      "35.975250",
      "139.752278"
    ],
    "Saitama Prefecture"
  ],
  [
    "Fujimino, Saitama",
    [
      "35.879528",
      "139.519778"
    ],
    "Saitama Prefecture"
  ],
  [
    "Fukaya, Saitama",
    [
      "36.197472",
      "139.281500"
    ],
    "Saitama Prefecture"
  ],
  [
    "Honj\u014d, Saitama",
    [
      "36.243583",
      "139.190389"
    ],
    "Saitama Prefecture"
  ],
  [
    "Shiraoka, Saitama",
    [
      "36.019056",
      "139.67694"
    ],
    "Saitama Prefecture"
  ],
  [
    "\u014ctsu, Shiga",
    [
      "35.017",
      "135.850"
    ],
    "Shiga Prefecture"
  ],
  [
    "Hikone, Shiga",
    [
      "35.267",
      "136.267"
    ],
    "Shiga Prefecture"
  ],
  [
    "Kusatsu, Shiga",
    [
      "35.017",
      "135.967"
    ],
    "Shiga Prefecture"
  ],
  [
    "Moriyama, Shiga",
    [
      "35.05861",
      "135.99417"
    ],
    "Shiga Prefecture"
  ],
  [
    "Ritt\u014d, Shiga",
    [
      "35.017",
      "136.000"
    ],
    "Shiga Prefecture"
  ],
  [
    "K\u014dka, Shiga",
    [
      "34.967",
      "136.167"
    ],
    "Shiga Prefecture"
  ],
  [
    "Yasu, Shiga",
    [
      "35.067",
      "136.033"
    ],
    "Shiga Prefecture"
  ],
  [
    "Konan, Shiga",
    [
      "35.000",
      "136.083"
    ],
    "Shiga Prefecture"
  ],
  [
    "Takashima, Shiga",
    [
      "35.350",
      "136.033"
    ],
    "Shiga Prefecture"
  ],
  [
    "Higashi\u014dmi, Shiga",
    [
      "35.117",
      "136.200"
    ],
    "Shiga Prefecture"
  ],
  [
    "Maibara, Shiga",
    [
      "35.317",
      "136.283"
    ],
    "Shiga Prefecture"
  ],
  [
    "Nagahama, Shiga",
    [
      "35.383",
      "136.283"
    ],
    "Shiga Prefecture"
  ],
  [
    "\u014cmihachiman, Shiga",
    [
      "35.12833",
      "136.09806"
    ],
    "Shiga Prefecture"
  ],
  [
    "Matsue, Shimane",
    [
      "35.47083",
      "133.05194"
    ],
    "Shimane Prefecture"
  ],
  [
    "Izumo, Shimane",
    [
      "35.367",
      "132.767"
    ],
    "Shimane Prefecture"
  ],
  [
    "Masuda, Shimane",
    [
      "34.667",
      "131.850"
    ],
    "Shimane Prefecture"
  ],
  [
    "Yasugi, Shimane",
    [
      "35.42833",
      "133.25361"
    ],
    "Shimane Prefecture"
  ],
  [
    "G\u014dtsu, Shimane",
    [
      "35.017",
      "132.217"
    ],
    "Shimane Prefecture"
  ],
  [
    "Unnan, Shimane",
    [
      "35.283",
      "132.900"
    ],
    "Shimane Prefecture"
  ],
  [
    "Hamada, Shimane",
    [
      "34.900",
      "132.083"
    ],
    "Shimane Prefecture"
  ],
  [
    "\u014cda, Shimane",
    [
      "35.183",
      "132.500"
    ],
    "Shimane Prefecture"
  ],
  [
    "Shizuoka, Shizuoka",
    [
      "34.97556",
      "138.38278"
    ],
    "Shizuoka Prefecture"
  ],
  [
    "Hamamatsu",
    [
      "34.71083",
      "137.72750"
    ],
    "Shizuoka Prefecture"
  ],
  [
    "Numazu, Shizuoka",
    [
      "35.095583",
      "138.863444"
    ],
    "Shizuoka Prefecture"
  ],
  [
    "Atami, Shizuoka",
    [
      "35.095972",
      "139.071556"
    ],
    "Shizuoka Prefecture"
  ],
  [
    "Mishima, Shizuoka",
    [
      "35.118500",
      "138.918556"
    ],
    "Shizuoka Prefecture"
  ],
  [
    "Fujinomiya, Shizuoka",
    [
      "35.222111",
      "138.621611"
    ],
    "Shizuoka Prefecture"
  ],
  [
    "It\u014d, Shizuoka",
    [
      "34.965722",
      "139.101861"
    ],
    "Shizuoka Prefecture"
  ],
  [
    "Shimada, Shizuoka",
    [
      "34.836278",
      "138.192722"
    ],
    "Shizuoka Prefecture"
  ],
  [
    "Iwata, Shizuoka",
    [
      "34.717889",
      "137.851528"
    ],
    "Shizuoka Prefecture"
  ],
  [
    "Yaizu, Shizuoka",
    [
      "34.86694",
      "138.32472"
    ],
    "Shizuoka Prefecture"
  ],
  [
    "Kakegawa, Shizuoka",
    [
      "34.768694",
      "137.998417"
    ],
    "Shizuoka Prefecture"
  ],
  [
    "Fujieda, Shizuoka",
    [
      "34.867417",
      "138.257722"
    ],
    "Shizuoka Prefecture"
  ],
  [
    "Gotemba, Shizuoka",
    [
      "35.308694",
      "138.934611"
    ],
    "Shizuoka Prefecture"
  ],
  [
    "Fukuroi, Shizuoka",
    [
      "34.750167",
      "137.924667"
    ],
    "Shizuoka Prefecture"
  ],
  [
    "Fuji, Shizuoka",
    [
      "35.161333",
      "138.676278"
    ],
    "Shizuoka Prefecture"
  ],
  [
    "Shimoda, Shizuoka",
    [
      "34.679528",
      "138.945306"
    ],
    "Shizuoka Prefecture"
  ],
  [
    "Susono, Shizuoka",
    [
      "35.173944",
      "138.906778"
    ],
    "Shizuoka Prefecture"
  ],
  [
    "Kosai, Shizuoka",
    [
      "34.718444",
      "137.531611"
    ],
    "Shizuoka Prefecture"
  ],
  [
    "Izu, Shizuoka",
    [
      "34.976528",
      "138.946806"
    ],
    "Shizuoka Prefecture"
  ],
  [
    "Omaezaki, Shizuoka",
    [
      "34.637944",
      "138.128083"
    ],
    "Shizuoka Prefecture"
  ],
  [
    "Kikugawa, Shizuoka",
    [
      "34.750",
      "138.083"
    ],
    "Shizuoka Prefecture"
  ],
  [
    "Izunokuni, Shizuoka",
    [
      "35.033",
      "138.933"
    ],
    "Shizuoka Prefecture"
  ],
  [
    "Makinohara, Shizuoka",
    [
      "34.733",
      "138.217"
    ],
    "Shizuoka Prefecture"
  ],
  [
    "Utsunomiya, Tochigi",
    [
      "36.555111",
      "139.882556"
    ],
    "Tochigi Prefecture"
  ],
  [
    "Ashikaga, Tochigi",
    [
      "36.340167",
      "139.44972"
    ],
    "Tochigi Prefecture"
  ],
  [
    "Tochigi, Tochigi",
    [
      "36.381333",
      "139.73028"
    ],
    "Tochigi Prefecture"
  ],
  [
    "Kanuma, Tochigi",
    [
      "36.567083",
      "139.745056"
    ],
    "Tochigi Prefecture"
  ],
  [
    "Oyama, Tochigi",
    [
      "36.314611",
      "139.800167"
    ],
    "Tochigi Prefecture"
  ],
  [
    "Mooka, Tochigi",
    [
      "36.440417",
      "140.013389"
    ],
    "Tochigi Prefecture"
  ],
  [
    "\u014ctawara, Tochigi",
    [
      "36.87111",
      "140.01556"
    ],
    "Tochigi Prefecture"
  ],
  [
    "Yaita, Tochigi",
    [
      "36.806722",
      "139.924111"
    ],
    "Tochigi Prefecture"
  ],
  [
    "Nasushiobara, Tochigi",
    [
      "36.961722",
      "140.046056"
    ],
    "Tochigi Prefecture"
  ],
  [
    "Sano, Tochigi",
    [
      "36.314500",
      "139.57833"
    ],
    "Tochigi Prefecture"
  ],
  [
    "Sakura, Tochigi",
    [
      "36.68528",
      "139.966417"
    ],
    "Tochigi Prefecture"
  ],
  [
    "Nasukarasuyama, Tochigi",
    [
      "36.656889",
      "140.151417"
    ],
    "Tochigi Prefecture"
  ],
  [
    "Shimotsuke, Tochigi",
    [
      "36.387194",
      "139.842056"
    ],
    "Tochigi Prefecture"
  ],
  [
    "Nikk\u014d, Tochigi",
    [
      "36.719833",
      "139.698167"
    ],
    "Tochigi Prefecture"
  ],
  [
    "Tokushima, Tokushima",
    "Tokushima Prefecture"
  ],
  [
    "Naruto, Tokushima",
    [
      "34.167",
      "134.617"
    ],
    "Tokushima Prefecture"
  ],
  [
    "Komatsushima, Tokushima",
    [
      "34.00028",
      "134.58444"
    ],
    "Tokushima Prefecture"
  ],
  [
    "Anan, Tokushima",
    [
      "33.917",
      "134.667"
    ],
    "Tokushima Prefecture"
  ],
  [
    "Yoshinogawa, Tokushima",
    [
      "34.06306",
      "134.36139"
    ],
    "Tokushima Prefecture"
  ],
  [
    "Mima, Tokushima",
    [
      "34.050",
      "134.167"
    ],
    "Tokushima Prefecture"
  ],
  [
    "Awa, Tokushima",
    [
      "34.10139",
      "134.29639"
    ],
    "Tokushima Prefecture"
  ],
  [
    "Miyoshi, Tokushima",
    [
      "34.026028",
      "133.807167"
    ],
    "Tokushima Prefecture"
  ],
  [
    "Hachi\u014dji, Tokyo",
    [
      "35.666444",
      "139.316000"
    ],
    "Tokyo",
    [
      "35.68972",
      "139.69222"
    ]
  ],
  [
    "Tachikawa, Tokyo",
    [
      "35.694222",
      "139.419667"
    ],
    "Tokyo",
    [
      "35.68972",
      "139.69222"
    ]
  ],
  [
    "Musashino, Tokyo",
    [
      "35.717722",
      "139.566056"
    ],
    "Tokyo",
    [
      "35.68972",
      "139.69222"
    ]
  ],
  [
    "Mitaka, Tokyo",
    [
      "35.683556",
      "139.559528"
    ],
    "Tokyo",
    [
      "35.68972",
      "139.69222"
    ]
  ],
  [
    "\u014cme, Tokyo",
    [
      "35.787972",
      "139.27583"
    ],
    "Tokyo",
    [
      "35.68972",
      "139.69222"
    ]
  ],
  [
    "Fuch\u016b, Tokyo",
    [
      "35.668944",
      "139.477639"
    ],
    "Tokyo",
    [
      "35.68972",
      "139.69222"
    ]
  ],
  [
    "Akishima, Tokyo",
    [
      "35.705667",
      "139.353528"
    ],
    "Tokyo",
    [
      "35.68972",
      "139.69222"
    ]
  ],
  [
    "Ch\u014dfu, Tokyo",
    [
      "35.6506139",
      "139.540667"
    ],
    "Tokyo",
    [
      "35.68972",
      "139.69222"
    ]
  ],
  [
    "Machida, Tokyo",
    [
      "35.55417",
      "139.44306"
    ],
    "Tokyo",
    [
      "35.68972",
      "139.69222"
    ]
  ],
  [
    "Koganei, Tokyo",
    [
      "35.699472",
      "139.502972"
    ],
    "Tokyo",
    [
      "35.68972",
      "139.69222"
    ]
  ],
  [
    "Kodaira, Tokyo",
    [
      "35.728500",
      "139.477444"
    ],
    "Tokyo",
    [
      "35.68972",
      "139.69222"
    ]
  ],
  [
    "Hino, Tokyo",
    [
      "35.671278",
      "139.395139"
    ],
    "Tokyo",
    [
      "35.68972",
      "139.69222"
    ]
  ],
  [
    "Higashimurayama, Tokyo",
    [
      "35.754611",
      "139.468500"
    ],
    "Tokyo",
    [
      "35.68972",
      "139.69222"
    ]
  ],
  [
    "Kokubunji, Tokyo",
    [
      "35.710944",
      "139.462167"
    ],
    "Tokyo",
    [
      "35.68972",
      "139.69222"
    ]
  ],
  [
    "Kunitachi, Tokyo",
    [
      "35.683917",
      "139.44139"
    ],
    "Tokyo",
    [
      "35.68972",
      "139.69222"
    ]
  ],
  [
    "Fussa, Tokyo",
    [
      "35.733",
      "139.333"
    ],
    "Tokyo",
    [
      "35.68972",
      "139.69222"
    ]
  ],
  [
    "Komae, Tokyo",
    [
      "35.634778",
      "139.578694"
    ],
    "Tokyo",
    [
      "35.68972",
      "139.69222"
    ]
  ],
  [
    "Higashiyamato, Tokyo",
    [
      "35.745361",
      "139.426500"
    ],
    "Tokyo",
    [
      "35.68972",
      "139.69222"
    ]
  ],
  [
    "Kiyose, Tokyo",
    [
      "35.785722",
      "139.526472"
    ],
    "Tokyo",
    [
      "35.68972",
      "139.69222"
    ]
  ],
  [
    "Higashikurume, Tokyo",
    [
      "35.758000",
      "139.529861"
    ],
    "Tokyo",
    [
      "35.68972",
      "139.69222"
    ]
  ],
  [
    "Musashimurayama, Tokyo",
    [
      "35.754833",
      "139.387361"
    ],
    "Tokyo",
    [
      "35.68972",
      "139.69222"
    ]
  ],
  [
    "Tama, Tokyo",
    [
      "35.63694",
      "139.446278"
    ],
    "Tokyo",
    [
      "35.68972",
      "139.69222"
    ]
  ],
  [
    "Inagi, Tokyo",
    [
      "35.637944",
      "139.504556"
    ],
    "Tokyo",
    [
      "35.68972",
      "139.69222"
    ]
  ],
  [
    "Hamura, Tokyo",
    [
      "35.767167",
      "139.310944"
    ],
    "Tokyo",
    [
      "35.68972",
      "139.69222"
    ]
  ],
  [
    "Akiruno, Tokyo",
    [
      "35.728917",
      "139.294083"
    ],
    "Tokyo",
    [
      "35.68972",
      "139.69222"
    ]
  ],
  [
    "Nishit\u014dky\u014d, Tokyo",
    [
      "35.725611",
      "139.538250"
    ],
    "Tokyo",
    [
      "35.68972",
      "139.69222"
    ]
  ],
  [
    "Special wards of Tokyo",
    "Tokyo",
    [
      "35.68972",
      "139.69222"
    ]
  ],
  [
    "Adachi, Tokyo",
    [
      "35.783",
      "139.800"
    ],
    "Tokyo",
    [
      "35.68972",
      "139.69222"
    ]
  ],
  [
    "Arakawa, Tokyo",
    [
      "35.733",
      "139.783"
    ],
    "Tokyo",
    [
      "35.68972",
      "139.69222"
    ]
  ],
  [
    "Bunky\u014d",
    [
      "35.717",
      "139.750"
    ],
    "Tokyo",
    [
      "35.68972",
      "139.69222"
    ]
  ],
  [
    "Chiyoda, Tokyo",
    [
      "35.6940028",
      "139.7535944"
    ],
    "Tokyo",
    [
      "35.68972",
      "139.69222"
    ]
  ],
  [
    "Ch\u016b\u014d, Tokyo",
    [
      "35.667",
      "139.767"
    ],
    "Tokyo",
    [
      "35.68972",
      "139.69222"
    ]
  ],
  [
    "Edogawa, Tokyo",
    [
      "35.700",
      "139.883"
    ],
    "Tokyo",
    [
      "35.68972",
      "139.69222"
    ]
  ],
  [
    "Itabashi",
    [
      "35.767",
      "139.683"
    ],
    "Tokyo",
    [
      "35.68972",
      "139.69222"
    ]
  ],
  [
    "Katsushika",
    [
      "35.733",
      "139.850"
    ],
    "Tokyo",
    [
      "35.68972",
      "139.69222"
    ]
  ],
  [
    "Kita, Tokyo",
    [
      "35.750",
      "139.733"
    ],
    "Tokyo",
    [
      "35.68972",
      "139.69222"
    ]
  ],
  [
    "K\u014dt\u014d",
    [
      "35.667",
      "139.817"
    ],
    "Tokyo",
    [
      "35.68972",
      "139.69222"
    ]
  ],
  [
    "Meguro",
    [
      "35.633",
      "139.683"
    ],
    "Tokyo",
    [
      "35.68972",
      "139.69222"
    ]
  ],
  [
    "Minato, Tokyo",
    [
      "35.65806",
      "139.75139"
    ],
    "Tokyo",
    [
      "35.68972",
      "139.69222"
    ]
  ],
  [
    "Nakano, Tokyo",
    [
      "35.7073972",
      "139.6638361"
    ],
    "Tokyo",
    [
      "35.68972",
      "139.69222"
    ]
  ],
  [
    "Nerima",
    [
      "35.7356222",
      "139.6516583"
    ],
    "Tokyo",
    [
      "35.68972",
      "139.69222"
    ]
  ],
  [
    "\u014cta, Tokyo",
    [
      "35.56139",
      "139.71611"
    ],
    "Tokyo",
    [
      "35.68972",
      "139.69222"
    ]
  ],
  [
    "Setagaya",
    [
      "35.6465722",
      "139.6532472"
    ],
    "Tokyo",
    [
      "35.68972",
      "139.69222"
    ]
  ],
  [
    "Shibuya",
    [
      "35.65944",
      "139.70056"
    ],
    "Tokyo",
    [
      "35.68972",
      "139.69222"
    ]
  ],
  [
    "Shinagawa",
    [
      "35.600",
      "139.733"
    ],
    "Tokyo",
    [
      "35.68972",
      "139.69222"
    ]
  ],
  [
    "Shinjuku",
    [
      "35.70139",
      "139.70972"
    ],
    "Tokyo",
    [
      "35.68972",
      "139.69222"
    ]
  ],
  [
    "Suginami",
    [
      "35.69944",
      "139.63639"
    ],
    "Tokyo",
    [
      "35.68972",
      "139.69222"
    ]
  ],
  [
    "Sumida, Tokyo",
    [
      "35.700",
      "139.817"
    ],
    "Tokyo",
    [
      "35.68972",
      "139.69222"
    ]
  ],
  [
    "Tait\u014d",
    [
      "35.71250",
      "139.78000"
    ],
    "Tokyo",
    [
      "35.68972",
      "139.69222"
    ]
  ],
  [
    "Toshima",
    [
      "35.73333",
      "139.71667"
    ],
    "Tokyo",
    [
      "35.68972",
      "139.69222"
    ]
  ],
  [
    "Tottori (city)",
    [
      "35.500",
      "134.233"
    ],
    "Tottori Prefecture"
  ],
  [
    "Yonago",
    [
      "35.433",
      "133.333"
    ],
    "Tottori Prefecture"
  ],
  [
    "Kurayoshi, Tottori",
    [
      "35.433",
      "133.817"
    ],
    "Tottori Prefecture"
  ],
  [
    "Sakaiminato, Tottori",
    [
      "35.533",
      "133.233"
    ],
    "Tottori Prefecture"
  ],
  [
    "Toyama (city)",
    [
      "36.695917",
      "137.213694"
    ],
    "Toyama Prefecture"
  ],
  [
    "Uozu, Toyama",
    [
      "36.827306",
      "137.40917"
    ],
    "Toyama Prefecture"
  ],
  [
    "Himi, Toyama",
    [
      "36.85667",
      "136.97306"
    ],
    "Toyama Prefecture"
  ],
  [
    "Namerikawa, Toyama",
    [
      "36.764361",
      "137.341167"
    ],
    "Toyama Prefecture"
  ],
  [
    "Tonami, Toyama",
    [
      "36.64750",
      "136.96222"
    ],
    "Toyama Prefecture"
  ],
  [
    "Oyabe, Toyama",
    [
      "36.675528",
      "136.868694"
    ],
    "Toyama Prefecture"
  ],
  [
    "Nanto, Toyama",
    [
      "36.58778",
      "136.919389"
    ],
    "Toyama Prefecture"
  ],
  [
    "Takaoka, Toyama",
    [
      "36.754056",
      "137.025667"
    ],
    "Toyama Prefecture"
  ],
  [
    "Imizu",
    [
      "36.73056",
      "137.07556"
    ],
    "Toyama Prefecture"
  ],
  [
    "Kurobe, Toyama",
    [
      "36.867",
      "137.450"
    ],
    "Toyama Prefecture"
  ],
  [
    "Wakayama (city)",
    [
      "34.233",
      "135.167"
    ],
    "Wakayama Prefecture"
  ],
  [
    "Kainan, Wakayama",
    [
      "34.150",
      "135.217"
    ],
    "Wakayama Prefecture"
  ],
  [
    "Tanabe, Wakayama",
    [
      "33.733",
      "135.383"
    ],
    "Wakayama Prefecture"
  ],
  [
    "Gob\u014d, Wakayama",
    [
      "33.883",
      "135.150"
    ],
    "Wakayama Prefecture"
  ],
  [
    "Arida, Wakayama",
    [
      "34.083",
      "135.133"
    ],
    "Wakayama Prefecture"
  ],
  [
    "Shing\u016b, Wakayama",
    [
      "33.717",
      "136.000"
    ],
    "Wakayama Prefecture"
  ],
  [
    "Kinokawa, Wakayama",
    [
      "34.26639",
      "135.36528"
    ],
    "Wakayama Prefecture"
  ],
  [
    "Hashimoto, Wakayama",
    [
      "34.317",
      "135.600"
    ],
    "Wakayama Prefecture"
  ],
  [
    "Iwade, Wakayama",
    [
      "34.250",
      "135.317"
    ],
    "Wakayama Prefecture"
  ],
  [
    "Yamagata (city)",
    [
      "38.255417",
      "140.339611"
    ],
    "Yamagata Prefecture"
  ],
  [
    "Yonezawa, Yamagata",
    [
      "37.922250",
      "140.116778"
    ],
    "Yamagata Prefecture"
  ],
  [
    "Shinj\u014d, Yamagata",
    [
      "38.767",
      "140.300"
    ],
    "Yamagata Prefecture"
  ],
  [
    "Sagae",
    [
      "38.380917",
      "140.276028"
    ],
    "Yamagata Prefecture"
  ],
  [
    "Kaminoyama",
    [
      "38.149583",
      "140.267861"
    ],
    "Yamagata Prefecture"
  ],
  [
    "Murayama, Yamagata",
    [
      "38.483",
      "140.383"
    ],
    "Yamagata Prefecture"
  ],
  [
    "Nagai, Yamagata",
    [
      "38.10750",
      "140.040528"
    ],
    "Yamagata Prefecture"
  ],
  [
    "Tend\u014d, Yamagata",
    [
      "38.362278",
      "140.377944"
    ],
    "Yamagata Prefecture"
  ],
  [
    "Higashine",
    [
      "38.431306",
      "140.391083"
    ],
    "Yamagata Prefecture"
  ],
  [
    "Obanazawa",
    [
      "38.600",
      "140.400"
    ],
    "Yamagata Prefecture"
  ],
  [
    "Nan'y\u014d, Yamagata",
    [
      "38.055111",
      "140.147611"
    ],
    "Yamagata Prefecture"
  ],
  [
    "Tsuruoka",
    [
      "38.72722",
      "139.82667"
    ],
    "Yamagata Prefecture"
  ],
  [
    "Sakata, Yamagata",
    [
      "38.914472",
      "139.836444"
    ],
    "Yamagata Prefecture"
  ],
  [
    "Ube, Yamaguchi",
    [
      "33.95167",
      "131.24667"
    ],
    "Yamaguchi Prefecture"
  ],
  [
    "H\u014dfu",
    [
      "34.05139",
      "131.56250"
    ],
    "Yamaguchi Prefecture"
  ],
  [
    "Kudamatsu",
    [
      "34.01500",
      "131.87028"
    ],
    "Yamaguchi Prefecture"
  ],
  [
    "Sh\u016bnan",
    [
      "34.05500",
      "131.80611"
    ],
    "Yamaguchi Prefecture"
  ],
  [
    "Hikari, Yamaguchi",
    [
      "33.96194",
      "131.94222"
    ],
    "Yamaguchi Prefecture"
  ],
  [
    "Shimonoseki",
    [
      "33.950",
      "130.933"
    ],
    "Yamaguchi Prefecture"
  ],
  [
    "Yanai, Yamaguchi",
    [
      "33.96389",
      "132.11861"
    ],
    "Yamaguchi Prefecture"
  ],
  [
    "Hagi, Yamaguchi",
    [
      "34.400",
      "131.400"
    ],
    "Yamaguchi Prefecture"
  ],
  [
    "Nagato, Yamaguchi",
    [
      "34.37222",
      "131.18333"
    ],
    "Yamaguchi Prefecture"
  ],
  [
    "San'y\u014d-Onoda",
    [
      "34.00306",
      "131.18194"
    ],
    "Yamaguchi Prefecture"
  ],
  [
    "Yamaguchi (city)",
    [
      "34.17806",
      "131.47389"
    ],
    "Yamaguchi Prefecture"
  ],
  [
    "Iwakuni",
    [
      "34.16639",
      "132.21889"
    ],
    "Yamaguchi Prefecture"
  ],
  [
    "Mine, Yamaguchi",
    [
      "34.16306",
      "131.20833"
    ],
    "Yamaguchi Prefecture"
  ],
  [
    "K\u014dfu",
    [
      "35.662139",
      "138.568222"
    ],
    "Yamanashi Prefecture"
  ],
  [
    "Fujiyoshida",
    [
      "35.487528",
      "138.807750"
    ],
    "Yamanashi Prefecture"
  ],
  [
    "Tsuru, Yamanashi",
    [
      "35.551528",
      "138.905444"
    ],
    "Yamanashi Prefecture"
  ],
  [
    "\u014ctsuki, Yamanashi",
    [
      "35.61056",
      "138.94000"
    ],
    "Yamanashi Prefecture"
  ],
  [
    "Nirasaki, Yamanashi",
    [
      "35.708861",
      "138.446139"
    ],
    "Yamanashi Prefecture"
  ],
  [
    "Minami-Alps, Yamanashi",
    [
      "35.608306",
      "138.465028"
    ],
    "Yamanashi Prefecture"
  ],
  [
    "Kai, Yamanashi",
    [
      "35.660806",
      "138.515778"
    ],
    "Yamanashi Prefecture"
  ],
  [
    "Fuefuki",
    [
      "35.647306",
      "138.63972"
    ],
    "Yamanashi Prefecture"
  ],
  [
    "Hokuto, Yamanashi",
    [
      "35.776472",
      "138.423639"
    ],
    "Yamanashi Prefecture"
  ],
  [
    "Uenohara",
    [
      "35.630194",
      "139.111333"
    ],
    "Yamanashi Prefecture"
  ],
  [
    "Yamanashi, Yamanashi",
    [
      "35.693444",
      "138.686889"
    ],
    "Yamanashi Prefecture"
  ],
  [
    "K\u014dsh\u016b, Yamanashi",
    [
      "35.704333",
      "138.729417"
    ],
    "Yamanashi Prefecture"
  ],
  [
    "Ch\u016b\u014d, Yamanashi",
    [
      "35.599611",
      "138.633917"
    ],
    "Yamanashi Prefecture"
  ]
]
prefecture_area_dict = {'Hokkaido': '83424.31', 'Iwate': '15275.01', 'Fukushima': '13783.74', 'Nagano': '13561.56', 'Niigata': '12584.10', 'Akita': '11637.54', 'Gifu': '10621.29', 'Aomori': '9645.59', 'Yamagata': '9323.15', 'Kagoshima': '9186.94', 'Hiroshima': '8479.45', 'Hyogo': '8400.96', 'Shizuoka': '7777.42', 'Miyazaki': '7735.31', 'Kumamoto': '7409.35', 'Miyagi': '7282.22', 'Okayama': '7114.50', 'Kochi': '7103.93', 'Shimane': '6708.24', 'Tochigi': '6408.09', 'Gunma': '6362.28', 'Oita': '6340.71', 'Yamaguchi': '6112.30', 'Ibaraki': '6097.06', 'Mie': '5774.40', 'Ehime': '5676.11', 'Aichi': '5172.48', 'Chiba': '5157.65', 'Fukuoka': '4986.40', 'Wakayama': '4724.69', 'Kyoto': '4612.19', 'Yamanashi': '4465.27', 'Toyama': '4247.61', 'Fukui': '4190.49', 'Ishikawa': '4186.09', 'Tokushima': '4146.65', 'Nagasaki': '4132.09', 'Shiga': '4017.38', 'Saitama': '3797.75', 'Nara': '3690.94', 'Tottori': '3507.05', 'Saga': '2440.68', 'Kanagawa': '2415.83', 'Okinawa': '2281.12', 'Tokyo': '2190.93', 'Osaka': '1905.14', 'Kagawa': '1876.72'}
prefecture_pop_dict = {'Akita': 152, 'Aomori': 366, 'Fukushima': 248, 'Iwate': 166, 'Miyagi': 552, 'Yamagata': 139, 'Chiba': 2002, 'Gunma': 418, 'Ibaraki': 628, 'Kanagawa': 5381, 'Saitama': 1590, 'Tochigi': 417, 'Tokyo': 16507, 'Aichi': 1852, 'Fukui': 144, 'Gifu': 305, 'Ishikawa': 247, 'Nagano': 486, 'Niigata': 292, 'Shizuoka': 759, 'Toyama': 146, 'Yamanashi': 251, 'Kyoto': 1210, 'Mie': 220, 'Nara': 283, 'Osaka': 2522, 'Shiga': 272, 'Wakayama': 147, 'Hiroshima': 623, 'Okayama': 329, 'Shimane': 130, 'Tottori': 62, 'Yamaguchi': 341, 'Ehime': 152, 'Kagawa': 155, 'Tokushima': 125, 'Fukuoka': 1144, 'Kagoshima': 226, 'Kumamoto': 281, 'Miyazaki': 170, 'Nagasaki': 440, 'Okinawa': 2886, 'Saga': 102, 'Hokkaido': 1090, 'Hyogo': 1585, 'Kochi': 137, 'Oita': 195}
tile_pdf_dict =  {895: 0.3580488, 865: 0.3580488, 823: 0.3580488, 866: 0.3580488, 821: 0.3580488, 825: 0.3580488, 897: 0.3580488, 46: 0.1064836, 57: 0.1064836, 58: 0.1064836, 59: 0.1064836, 60: 0.1064836, 61: 0.1064836, 62: 0.1064836, 864: 0.3580488, 869: 0.3580488, 862: 0.3580488, 858: 0.3580488, 859: 0.3580488, 860: 0.3580488, 818: 0.3580488, 512: 0.0192851, 824: 0.3580488, 820: 0.3580488, 861: 0.3580488, 898: 0.3580488, 899: 0.3580488, 900: 0.3580488, 932: 0.3580488, 933: 0.3580488, 936: 0.3580488, 819: 0.3580488, 402: 0.0301448, 433: 0.0301448, 434: 0.0301448, 437: 0.0301448, 516: 0.0301448, 517: 0.0301448, 518: 0.0301448, 519: 0.0301448, 523: 0.0301448, 863: 0.0301448, 822: 0.3580488, 1512: 0.0130612, 1513: 0.0130612, 1517: 0.0130612, 1605: 0.0130612, 1601: 0.0130612, 1602: 0.0130612, 1603: 0.0130612, 1604: 0.0130612, 1607: 0.0130612, 1608: 0.0130612, 1672: 0.0130612, 1675: 0.0130612, 1400: 0.0130612, 1499: 0.0130612, 1502: 0.0130612, 1503: 0.0130612, 1505: 0.0130612, 1506: 0.0130612, 1313: 0.0130612, 1314: 0.0130612, 1317: 0.0130612, 1399: 0.0130612, 1402: 0.0130612, 1403: 0.0130612, 1404: 0.0130612, 1405: 0.0130612, 1408: 0.0130612, 1409: 0.0130612, 1413: 0.0130612, 1507: 0.0130612, 1510: 0.0130612, 1511: 0.0130612, 1514: 0.0130612, 1312: 0.0130612, 1315: 0.0130612, 1310: 0.0130612, 1394: 0.0130612, 1395: 0.0130612, 1396: 0.0130612, 1397: 0.0130612, 1398: 0.0130612, 1401: 0.0130612, 1392: 0.0130612, 1494: 0.0130612, 1495: 0.0130612, 1496: 0.0130612, 1497: 0.0130612, 1498: 0.0130612, 1585: 0.0130612, 1586: 0.0130612, 1504: 0.0130612, 1508: 0.0130612, 1509: 0.0130612, 1593: 0.0130612, 1594: 0.0130612, 1595: 0.0130612, 1596: 0.0130612, 1597: 0.0130612, 1598: 0.0130612, 1600: 0.0130612, 1500: 0.0130612, 1501: 0.0130612, 1589: 0.0130612, 1590: 0.0130612, 1306: 0.0130612, 1307: 0.0130612, 1309: 0.0130612, 1311: 0.0130612, 1391: 0.0130612, 1316: 0.0130612, 1318: 0.0130612, 1320: 0.0130612, 1406: 0.0130612, 1407: 0.0130612, 1410: 0.0130612, 1411: 0.0130612, 1520: 0.0379448, 1609: 0.0379448, 1612: 0.0379448, 1744: 0.0379448, 1745: 0.0379448, 1746: 0.0379448, 1791: 0.0379448, 1618: 0.0379448, 1622: 0.0379448, 1685: 0.0379448, 1687: 0.0379448, 1688: 0.0379448, 1689: 0.0379448, 1690: 0.0379448, 1691: 0.0379448, 1692: 0.0379448, 1747: 0.0379448, 1748: 0.0379448, 1749: 0.0379448, 1750: 0.0379448, 1676: 0.0379448, 1677: 0.0379448, 1679: 0.0379448, 1680: 0.0379448, 1681: 0.0379448, 1682: 0.0379448, 1686: 0.0379448, 1740: 0.0379448, 1743: 0.0379448, 1319: 0.0379448, 1414: 0.0379448, 1415: 0.0379448, 1416: 0.0379448, 1418: 0.0379448, 1419: 0.0379448, 1420: 0.0379448, 1421: 0.0379448, 1422: 0.0379448, 1519: 0.0379448, 1522: 0.0379448, 1523: 0.0379448, 1526: 0.0379448, 1527: 0.0379448, 1524: 0.0379448, 1525: 0.0379448, 1528: 0.0379448, 1529: 0.0379448, 1610: 0.0379448, 1611: 0.0379448, 1613: 0.0379448, 1614: 0.0379448, 1615: 0.0379448, 1616: 0.0379448, 1617: 0.0379448, 1683: 0.0379448, 1684: 0.0379448, 1516: 0.0379448, 1521: 0.0379448, 1606: 0.0379448, 1412: 0.0379448, 1417: 0.0379448, 1515: 0.0379448, 1518: 0.0379448, 1260: 0.3881613, 1246: 0.3881613, 1248: 0.3881613, 1336: 0.3881613, 1341: 0.3881613, 1446: 0.3881613, 1271: 0.065074, 1345: 0.065074, 1337: 0.3881613, 1338: 0.3881613, 1259: 0.3881613, 1342: 0.3881613, 1251: 0.3881613, 1249: 0.3881613, 1250: 0.3881613, 1252: 0.3881613, 1255: 0.3881613, 1340: 0.3881613, 1256: 0.3881613, 1335: 0.3881613, 1334: 0.3881613, 1552: 0.3881613, 1449: 0.3881613, 1247: 0.3881613, 1339: 0.3881613, 1445: 0.3881613, 460: 0.0267789, 461: 0.0267789, 487: 0.0267789, 488: 0.0267789, 489: 0.0267789, 490: 0.0267789, 347: 0.0267789, 377: 0.0267789, 418: 0.0267789, 419: 0.0267789, 420: 0.0267789, 421: 0.0267789, 422: 0.0267789, 425: 0.0267789, 455: 0.0267789, 456: 0.0267789, 458: 0.0267789, 459: 0.0267789, 378: 0.0267789, 379: 0.0267789, 381: 0.0267789, 415: 0.0267789, 423: 0.0267789, 424: 0.0267789, 426: 0.0267789, 346: 0.0267789, 348: 0.0267789, 349: 0.0267789, 350: 0.0267789, 382: 0.0267789, 383: 0.0267789, 384: 0.0267789, 386: 0.0267789, 387: 0.0267789, 344: 0.0267789, 345: 0.0267789, 373: 0.0267789, 374: 0.0267789, 375: 0.0267789, 380: 0.0267789, 414: 0.0267789, 735: 0.0343635, 737: 0.0343635, 739: 0.0343635, 764: 0.0343635, 767: 0.0343635, 702: 0.0343635, 704: 0.0343635, 705: 0.0343635, 706: 0.0343635, 707: 0.0343635, 733: 0.0343635, 734: 0.0343635, 797: 0.0343635, 798: 0.0343635, 799: 0.0343635, 801: 0.0343635, 802: 0.0343635, 803: 0.0343635, 804: 0.0343635, 834: 0.0343635, 835: 0.0343635, 743: 0.0343635, 771: 0.0343635, 774: 0.0343635, 775: 0.0343635, 738: 0.0343635, 740: 0.0343635, 768: 0.0343635, 769: 0.0343635, 770: 0.0343635, 741: 1.3237872, 742: 1.3237872, 772: 1.3237872, 773: 1.3237872, 162: 0.229424, 165: 0.229424, 158: 0.229424, 213: 0.229424, 215: 0.229424, 160: 0.229424, 123: 0.229424, 214: 0.229424, 256: 0.229424, 255: 0.229424, 127: 0.229424, 163: 0.229424, 171: 0.229424, 216: 0.229424, 217: 0.229424, 219: 0.229424, 166: 0.229424, 172: 0.229424, 131: 0.1030005, 167: 0.1030005, 1262: 0.1030005, 170: 0.229424, 205: 0.229424, 208: 0.229424, 209: 0.229424, 168: 0.229424, 164: 0.229424, 169: 0.229424, 212: 0.229424, 159: 0.229424, 126: 0.229424, 129: 0.229424, 130: 0.229424, 132: 0.229424, 1475: 0.0179922, 1476: 0.0179922, 1478: 0.0179922, 1368: 0.0179922, 1369: 0.0179922, 1470: 0.0179922, 1467: 0.0179922, 1468: 0.0179922, 1469: 0.0179922, 1567: 0.0179922, 1646: 0.0179922, 1556: 0.0179922, 1557: 0.0179922, 1559: 0.0179922, 1560: 0.0179922, 1472: 0.0179922, 1473: 0.0179922, 1558: 0.0179922, 1561: 0.0179922, 1562: 0.0179922, 1564: 0.0179922, 1360: 0.0179922, 1363: 0.0179922, 1364: 0.0179922, 1365: 0.0179922, 1366: 0.0179922, 1463: 0.0179922, 1466: 0.0179922, 1474: 0.0179922, 1477: 0.0179922, 1563: 0.0179922, 1568: 0.0179922, 1643: 0.0179922, 1644: 0.0179922, 1645: 0.0179922, 1328: 0.0130657, 1329: 0.0130657, 1330: 0.0130657, 1331: 0.0130657, 1332: 0.0130657, 1333: 0.0130657, 1435: 0.0130657, 1437: 0.0130657, 1438: 0.0130657, 1439: 0.0130657, 1440: 0.0130657, 1441: 0.0130657, 1442: 0.0130657, 1443: 0.0130657, 1444: 0.0130657, 1481: 0.0130657, 1539: 0.0130657, 1540: 0.0130657, 1541: 0.0130657, 1542: 0.0130657, 1543: 0.0130657, 1544: 0.0130657, 1565: 0.0130657, 1566: 0.0130657, 1630: 0.0130657, 1631: 0.0130657, 1632: 0.0130657, 1633: 0.0130657, 1636: 0.0130657, 1695: 0.0130657, 1696: 0.0130657, 1699: 0.0130657, 1225: 0.0179922, 1226: 0.0179922, 1229: 0.0179922, 1230: 0.0179922, 1281: 0.0179922, 1282: 0.0179922, 1283: 0.0179922, 1284: 0.0179922, 1285: 0.0179922, 1286: 0.0179922, 1287: 0.0179922, 1288: 0.0179922, 1289: 0.0179922, 1367: 0.0179922, 1370: 0.0179922, 1373: 0.0179922, 1471: 0.0179922, 790: 0.0287159, 791: 0.0287159, 793: 0.0287159, 878: 0.0287159, 880: 0.0287159, 881: 0.0287159, 913: 0.0287159, 914: 0.0287159, 915: 0.0287159, 916: 0.0287159, 917: 0.0287159, 920: 0.0287159, 867: 0.0287159, 829: 0.0287159, 903: 0.0287159, 907: 0.0287159, 908: 0.0287159, 912: 0.0287159, 828: 0.0287159, 868: 0.0287159, 901: 0.0287159, 871: 0.0287159, 872: 0.0287159, 873: 0.0287159, 870: 0.0287159, 826: 0.0287159, 827: 0.0287159, 836: 0.0287159, 841: 0.0287159, 879: 0.0287159, 882: 0.0287159, 883: 0.0287159, 884: 0.0287159, 885: 0.0287159, 918: 0.0287159, 794: 0.0287159, 795: 0.0287159, 796: 0.0287159, 800: 0.0287159, 830: 0.0287159, 831: 0.0287159, 832: 0.0287159, 833: 0.0287159, 837: 0.0287159, 874: 0.0287159, 875: 0.0287159, 876: 0.0287159, 877: 0.0287159, 909: 0.0287159, 910: 0.0287159, 911: 0.0287159, 902: 0.0287159, 904: 0.0287159, 905: 0.0287159, 906: 0.0287159, 792: 0.0287159, 1208: 0.0656997, 1211: 0.0656997, 1162: 7.5342434, 1079: 0.0656997, 1122: 0.0656997, 1123: 0.0656997, 1124: 0.0656997, 1125: 0.0656997, 1126: 0.0656997, 1129: 0.0656997, 1163: 0.0656997, 1164: 0.0656997, 1165: 0.0656997, 1167: 0.0656997, 1169: 0.0656997, 1170: 0.0656997, 1116: 0.0656997, 1121: 0.0656997, 1120: 0.0656997, 1075: 0.0656997, 1080: 0.0656997, 1119: 0.0656997, 1071: 0.0656997, 1072: 0.0656997, 1076: 0.0656997, 1115: 0.0656997, 1118: 0.0656997, 1160: 0.0656997, 1161: 0.0656997, 1166: 0.0656997, 462: 0.0734717, 388: 0.0734717, 389: 0.0734717, 390: 0.0734717, 391: 0.0734717, 464: 0.0734717, 431: 0.0734717, 432: 0.0734717, 463: 7.5342434, 465: 7.5342434, 468: 7.5342434, 435: 0.0734717, 436: 0.0734717, 439: 0.0734717, 440: 0.0734717, 466: 0.0734717, 469: 0.0734717, 470: 0.0734717, 331: 0.0734717, 336: 0.0734717, 353: 0.0734717, 427: 0.0734717, 428: 0.0734717, 429: 0.0734717, 393: 0.0734717, 394: 0.0734717, 430: 0.0734717, 335: 0.0734717, 356: 0.0734717, 357: 0.0734717, 358: 0.0734717, 359: 0.0734717, 363: 0.0734717, 392: 0.0734717, 395: 0.0734717, 396: 0.0734717, 397: 0.0734717, 398: 0.0734717, 352: 0.0734717, 354: 0.0734717, 355: 0.0734717, 385: 0.0734717, 1619: 0.0130657, 1620: 0.0130657, 1621: 0.0130657, 1624: 0.0130657, 1628: 0.0130657, 1693: 0.0130657, 1694: 0.0130657, 1545: 0.0130657, 1546: 0.0130657, 1547: 0.0130657, 1548: 0.0130657, 1549: 0.0130657, 1550: 0.0130657, 1551: 0.0130657, 1634: 0.0130657, 1635: 0.0130657, 1637: 0.0130657, 1638: 0.0130657, 1639: 0.0130657, 1640: 0.0130657, 1641: 0.0130657, 1642: 0.0130657, 1700: 0.0130657, 1701: 0.0130657, 1703: 0.0130657, 1704: 0.0130657, 1705: 0.0130657, 1706: 0.0130657, 1902: 0.0130657, 1905: 0.0130657, 1906: 0.0130657, 1907: 0.0130657, 1946: 0.0130657, 1947: 0.0130657, 1948: 0.0130657, 1950: 0.0130657, 1951: 0.0130657, 1952: 0.0130657, 1953: 0.0130657, 1990: 0.0130657, 1991: 0.0130657, 1993: 0.0130657, 1994: 0.0130657, 1996: 0.0130657, 1627: 0.0130657, 1629: 0.0130657, 1928: 0.0130657, 1929: 0.0130657, 1932: 0.0130657, 1933: 0.0130657, 1937: 0.0130657, 1969: 0.0130657, 1970: 0.0130657, 1971: 0.0130657, 1972: 0.0130657, 1973: 0.0130657, 1974: 0.0130657, 1975: 0.0130657, 1976: 0.0130657, 1977: 0.0130657, 1978: 0.0130657, 1979: 0.0130657, 1980: 0.0130657, 1981: 0.0130657, 1983: 0.0130657, 1984: 0.0130657, 1988: 0.0130657, 2008: 0.0130657, 2009: 0.0130657, 2010: 0.0130657, 2011: 0.0130657, 2012: 0.0130657, 2013: 0.0130657, 2014: 0.0130657, 2015: 0.0130657, 2016: 0.0130657, 2017: 0.0130657, 2018: 0.0130657, 2019: 0.0130657, 2020: 0.0130657, 2021: 0.0130657, 2022: 0.0130657, 2023: 0.0130657, 2024: 0.0130657, 2025: 0.0130657, 2026: 0.0130657, 2027: 0.0130657, 2028: 0.0130657, 2029: 0.0130657, 2030: 0.0130657, 2033: 0.0130657, 2046: 0.0130657, 2047: 0.0130657, 2048: 0.0130657, 2049: 0.0130657, 2050: 0.0130657, 2051: 0.0130657, 2052: 0.0130657, 2053: 0.0130657, 2054: 0.0130657, 2055: 0.0130657, 2056: 0.0130657, 2058: 0.0130657, 2071: 0.0130657, 2072: 0.0130657, 2074: 0.0130657, 2075: 0.0130657, 1842: 0.0130657, 1843: 0.0130657, 1844: 0.0130657, 1845: 0.0130657, 1847: 0.0130657, 1848: 0.0130657, 1885: 0.0130657, 1886: 0.0130657, 1887: 0.0130657, 1888: 0.0130657, 1889: 0.0130657, 1890: 0.0130657, 1891: 0.0130657, 1892: 0.0130657, 1893: 0.0130657, 1927: 0.0130657, 1930: 0.0130657, 1931: 0.0130657, 1934: 0.0130657, 1799: 0.0130657, 1804: 0.0130657, 2108: 0.0130657, 2109: 0.0130657, 2110: 0.0130657, 2111: 0.0130657, 2112: 0.0130657, 2121: 0.0130657, 2122: 0.0130657, 2123: 0.0130657, 2124: 0.0130657, 2125: 0.0130657, 2126: 0.0130657, 2127: 0.0130657, 2128: 0.0130657, 2136: 0.0130657, 2137: 0.0130657, 2138: 0.0130657, 2139: 0.0130657, 2140: 0.0130657, 2141: 0.0130657, 2142: 0.0130657, 2143: 0.0130657, 2151: 0.0130657, 2154: 0.0130657, 2155: 0.0130657, 2156: 0.0130657, 2158: 0.0130657, 2159: 0.0130657, 2160: 0.0130657, 2161: 0.0130657, 2168: 0.0130657, 2170: 0.0130657, 1765: 0.0130657, 1766: 0.0130657, 1768: 0.0130657, 1769: 0.0130657, 1770: 0.0130657, 1806: 0.0130657, 1809: 0.0130657, 1810: 0.0130657, 1811: 0.0130657, 1812: 0.0130657, 1813: 0.0130657, 1814: 0.0130657, 1815: 0.0130657, 1816: 0.0130657, 1817: 0.0130657, 1818: 0.0130657, 1819: 0.0130657, 1821: 0.0130657, 1858: 0.0130657, 1861: 0.0130657, 1862: 0.0130657, 1865: 0.0130657, 1752: 0.0130657, 1839: 0.0130657, 1884: 0.0130657, 1707: 0.0130657, 1708: 0.0130657, 1709: 0.0130657, 1710: 0.0130657, 1820: 0.0130657, 1822: 0.0130657, 1823: 0.0130657, 1824: 0.0130657, 1825: 0.0130657, 1826: 0.0130657, 1827: 0.0130657, 1828: 0.0130657, 1829: 0.0130657, 1830: 0.0130657, 1831: 0.0130657, 1870: 0.0130657, 1873: 0.0130657, 1874: 0.0130657, 1875: 0.0130657, 1876: 0.0130657, 1877: 0.0130657, 1878: 0.0130657, 1879: 0.0130657, 1880: 0.0130657, 1881: 0.0130657, 1882: 0.0130657, 1883: 0.0130657, 1921: 0.0130657, 1924: 0.0130657, 1925: 0.0130657, 1926: 0.0130657, 1802: 0.0130657, 1803: 0.0130657, 1897: 0.0130657, 1900: 0.0130657, 1903: 0.0130657, 1759: 0.0130657, 1760: 0.0130657, 1798: 0.0130657, 1801: 0.0130657, 1856: 0.0130657, 1995: 0.0130657, 1999: 0.0130657, 2000: 0.0130657, 2003: 0.0130657, 2004: 0.0130657, 2007: 0.0130657, 2031: 0.0130657, 2032: 0.0130657, 2034: 0.0130657, 2035: 0.0130657, 2036: 0.0130657, 2037: 0.0130657, 2038: 0.0130657, 2039: 0.0130657, 2040: 0.0130657, 2041: 0.0130657, 2042: 0.0130657, 2043: 0.0130657, 2044: 0.0130657, 2045: 0.0130657, 2064: 0.0130657, 2067: 0.0130657, 2068: 0.0130657, 2069: 0.0130657, 2070: 0.0130657, 2091: 0.0130657, 1846: 0.0130657, 1849: 0.0130657, 1852: 0.0130657, 2145: 0.0130657, 2148: 0.0130657, 2149: 0.0130657, 2150: 0.0130657, 2152: 0.0130657, 2153: 0.0130657, 2157: 0.0130657, 2162: 0.0130657, 2163: 0.0130657, 2164: 0.0130657, 2165: 0.0130657, 2166: 0.0130657, 2167: 0.0130657, 2169: 0.0130657, 2171: 0.0130657, 2172: 0.0130657, 2173: 0.0130657, 2174: 0.0130657, 2175: 0.0130657, 2176: 0.0130657, 2177: 0.0130657, 2178: 0.0130657, 2179: 0.0130657, 2180: 0.0130657, 2181: 0.0130657, 2182: 0.0130657, 2183: 0.0130657, 2184: 0.0130657, 2185: 0.0130657, 2186: 0.0130657, 2187: 0.0130657, 1793: 0.0130657, 1795: 0.0130657, 1796: 0.0130657, 1840: 0.0130657, 1841: 0.0130657, 1807: 0.0130657, 1853: 0.0130657, 1854: 0.0130657, 1805: 0.0130657, 1808: 0.0130657, 1850: 0.0130657, 1851: 0.0130657, 1855: 0.0130657, 1857: 0.0130657, 1859: 0.0130657, 1860: 0.0130657, 1864: 0.0130657, 1901: 0.0130657, 1904: 0.0130657, 1894: 0.0130657, 1895: 0.0130657, 1896: 0.0130657, 1898: 0.0130657, 1899: 0.0130657, 1935: 0.0130657, 1936: 0.0130657, 1938: 0.0130657, 1939: 0.0130657, 1940: 0.0130657, 1941: 0.0130657, 1942: 0.0130657, 1943: 0.0130657, 1944: 0.0130657, 1945: 0.0130657, 1949: 0.0130657, 1982: 0.0130657, 1985: 0.0130657, 1986: 0.0130657, 1987: 0.0130657, 1989: 0.0130657, 1992: 0.0130657, 1697: 0.0130657, 1698: 0.0130657, 1702: 0.0130657, 1751: 0.0130657, 1753: 0.0130657, 1755: 0.0130657, 1756: 0.0130657, 1794: 0.0130657, 1797: 0.0130657, 1800: 0.0130657, 1754: 0.0130657, 1757: 0.0130657, 1758: 0.0130657, 1761: 0.0130657, 1762: 0.0130657, 1763: 0.0130657, 1764: 0.0130657, 1767: 0.0130657, 4: 0.0130657, 2073: 0.0130657, 2076: 0.0130657, 2077: 0.0130657, 2094: 0.0130657, 2095: 0.0130657, 2096: 0.0130657, 2097: 0.0130657, 2098: 0.0130657, 2101: 0.0130657, 2113: 0.0130657, 2114: 0.0130657, 2115: 0.0130657, 2116: 0.0130657, 2117: 0.0130657, 2118: 0.0130657, 2119: 0.0130657, 2120: 0.0130657, 2129: 0.0130657, 2130: 0.0130657, 2131: 0.0130657, 2132: 0.0130657, 2133: 0.0130657, 2134: 0.0130657, 2135: 0.0130657, 2144: 0.0130657, 2146: 0.0130657, 2147: 0.0130657, 1019: 0.0562116, 1021: 0.0562116, 1026: 0.0562116, 1066: 0.0562116, 1191: 0.0562116, 1321: 0.0562116, 1322: 0.0562116, 1323: 0.0562116, 1324: 0.0562116, 1325: 0.0562116, 1326: 0.0562116, 1327: 0.0562116, 1423: 0.0562116, 1424: 0.0562116, 1425: 0.0562116, 1426: 0.0562116, 1427: 0.0562116, 1428: 0.0562116, 1429: 0.0562116, 1430: 0.0562116, 1431: 0.0562116, 1432: 0.0562116, 1433: 0.0562116, 1434: 0.0562116, 1436: 0.0562116, 1530: 0.0562116, 1531: 0.0562116, 1532: 0.0562116, 1533: 0.0562116, 1534: 0.0562116, 1535: 0.0562116, 1536: 0.0562116, 1537: 0.0562116, 1538: 0.0562116, 1623: 0.0562116, 1625: 0.0562116, 1626: 0.0562116, 2057: 0.0130657, 2059: 0.0130657, 2060: 0.0130657, 2061: 0.0130657, 2062: 0.0130657, 2063: 0.0130657, 2065: 0.0130657, 2066: 0.0130657, 2078: 0.0130657, 2079: 0.0130657, 2080: 0.0130657, 2081: 0.0130657, 2082: 0.0130657, 2083: 0.0130657, 2084: 0.0130657, 2085: 0.0130657, 2086: 0.0130657, 2087: 0.0130657, 2088: 0.0130657, 2089: 0.0130657, 2090: 0.0130657, 2092: 0.0130657, 2093: 0.0130657, 2099: 0.0130657, 2100: 0.0130657, 2102: 0.0130657, 2103: 0.0130657, 2104: 0.0130657, 2105: 0.0130657, 2106: 0.0130657, 2107: 0.0130657, 1863: 0.0130657, 1866: 0.0130657, 1867: 0.0130657, 1868: 0.0130657, 1869: 0.0130657, 1871: 0.0130657, 1872: 0.0130657, 1908: 0.0130657, 1909: 0.0130657, 1910: 0.0130657, 1911: 0.0130657, 1912: 0.0130657, 1913: 0.0130657, 1914: 0.0130657, 1915: 0.0130657, 1916: 0.0130657, 1917: 0.0130657, 1918: 0.0130657, 1919: 0.0130657, 1920: 0.0130657, 1922: 0.0130657, 1923: 0.0130657, 1954: 0.0130657, 1955: 0.0130657, 1956: 0.0130657, 1957: 0.0130657, 1958: 0.0130657, 1959: 0.0130657, 1960: 0.0130657, 1961: 0.0130657, 1962: 0.0130657, 1963: 0.0130657, 1964: 0.0130657, 1965: 0.0130657, 1966: 0.0130657, 1967: 0.0130657, 1968: 0.0130657, 1997: 0.0130657, 1998: 0.0130657, 2001: 0.0130657, 2002: 0.0130657, 2005: 0.0130657, 2006: 0.0130657, 602: 0.1886689, 605: 0.1886689, 663: 0.1886689, 628: 0.1886689, 660: 0.1886689, 662: 0.1886689, 585: 0.1886689, 595: 0.1886689, 614: 0.1886689, 615: 0.1886689, 616: 0.1886689, 617: 0.1886689, 618: 0.1886689, 639: 0.1886689, 603: 0.1886689, 604: 0.1886689, 661: 0.1886689, 629: 0.1886689, 630: 0.1886689, 667: 0.1886689, 634: 0.1886689, 664: 0.1886689, 607: 0.1886689, 608: 0.1886689, 633: 0.1886689, 665: 0.1886689, 591: 0.1886689, 593: 0.1886689, 594: 0.1886689, 596: 0.1886689, 609: 0.1886689, 610: 0.1886689, 613: 0.1886689, 635: 0.1886689, 638: 0.1886689, 597: 0.1886689, 598: 0.1886689, 599: 0.1886689, 611: 0.1886689, 612: 0.1886689, 636: 0.1886689, 600: 0.1886689, 625: 0.1886689, 626: 0.1886689, 586: 0.1886689, 587: 0.1886689, 588: 0.1886689, 589: 0.1886689, 590: 0.1886689, 592: 0.1886689, 606: 0.1886689, 632: 0.1886689, 601: 0.1886689, 631: 0.1886689, 1349: 0.1030005, 1344: 0.1030005, 1263: 0.1030005, 1460: 0.1030005, 1461: 0.1030005, 1465: 0.1030005, 1464: 0.1030005, 1554: 0.1030005, 1555: 0.1030005, 1343: 0.1030005, 1347: 0.1030005, 1456: 0.1030005, 1457: 0.1030005, 1448: 0.1030005, 1458: 0.1030005, 1459: 0.1030005, 1462: 0.1030005, 1264: 0.1030005, 1447: 0.1030005, 1450: 0.1030005, 1268: 0.1030005, 1348: 0.1030005, 1553: 0.1030005, 1453: 0.1030005, 1350: 0.1030005, 1452: 0.1030005, 1352: 0.1030005, 1353: 0.1030005, 1455: 0.1030005, 1346: 0.1030005, 1451: 0.1030005, 1454: 0.1030005, 812: 0.0590049, 839: 0.0590049, 848: 0.0590049, 853: 0.0590049, 805: 0.0590049, 806: 0.0590049, 893: 0.0590049, 894: 0.0590049, 813: 0.0590049, 816: 0.0590049, 846: 0.0590049, 847: 0.0590049, 850: 0.0590049, 811: 0.0590049, 814: 0.0590049, 843: 0.0590049, 809: 0.0590049, 810: 0.0590049, 807: 0.0590049, 808: 0.0590049, 838: 0.0590049, 776: 0.0590049, 777: 0.0590049, 778: 0.0590049, 815: 0.0590049, 817: 0.0590049, 851: 0.0590049, 852: 0.0590049, 854: 0.0590049, 855: 0.0590049, 856: 0.0590049, 857: 0.0590049, 892: 0.0590049, 1776: 0.0108674, 1777: 0.0108674, 1832: 0.0108674, 1833: 0.0108674, 1773: 0.0108674, 1721: 0.0108674, 1771: 0.0108674, 1772: 0.0108674, 1592: 0.0108674, 1659: 0.0108674, 1662: 0.0108674, 1723: 0.0108674, 1780: 0.0108674, 1781: 0.0108674, 1782: 0.0108674, 1785: 0.0108674, 1834: 0.0108674, 1835: 0.0108674, 1836: 0.0108674, 1837: 0.0108674, 1599: 0.0108674, 1668: 0.0108674, 1669: 0.0108674, 1671: 0.0108674, 1674: 0.0108674, 1732: 0.0108674, 1733: 0.0108674, 1588: 0.0108674, 1653: 0.0108674, 1655: 0.0108674, 1658: 0.0108674, 1719: 0.0108674, 1725: 0.0108674, 1726: 0.0108674, 1729: 0.0108674, 1730: 0.0108674, 1774: 0.0108674, 1775: 0.0108674, 1778: 0.0108674, 1779: 0.0108674, 1591: 0.0108674, 1660: 0.0108674, 1661: 0.0108674, 1663: 0.0108674, 1666: 0.0108674, 1724: 0.0108674, 1727: 0.0108674, 1673: 0.0108674, 1678: 0.0108674, 1735: 0.0108674, 1736: 0.0108674, 1737: 0.0108674, 1738: 0.0108674, 1739: 0.0108674, 1741: 0.0108674, 1742: 0.0108674, 1587: 0.0108674, 1656: 0.0108674, 1657: 0.0108674, 1720: 0.0108674, 1783: 0.0108674, 1784: 0.0108674, 1786: 0.0108674, 1787: 0.0108674, 1788: 0.0108674, 1789: 0.0108674, 1790: 0.0108674, 1792: 0.0108674, 1838: 0.0108674, 1664: 0.0108674, 1665: 0.0108674, 1667: 0.0108674, 1670: 0.0108674, 1728: 0.0108674, 1731: 0.0108674, 1734: 0.0108674, 524: 0.0825909, 522: 0.0825909, 527: 0.0825909, 521: 0.0825909, 555: 0.0825909, 556: 0.0825909, 558: 0.0825909, 561: 0.0825909, 582: 0.0825909, 583: 0.0825909, 492: 0.0825909, 491: 0.0825909, 520: 0.0825909, 178: 0.0246001, 179: 0.0246001, 180: 0.0246001, 183: 0.0246001, 68: 0.0246001, 84: 0.0246001, 107: 0.0246001, 108: 0.0246001, 110: 0.0246001, 111: 0.0246001, 109: 1.3237872, 142: 1.3237872, 143: 1.3237872, 134: 0.0246001, 177: 0.0246001, 101: 0.0246001, 103: 0.0246001, 5: 0.0246001, 6: 0.0246001, 7: 0.0246001, 8: 0.0246001, 173: 0.0246001, 174: 0.0246001, 175: 0.0246001, 176: 0.0246001, 137: 0.0246001, 181: 0.0246001, 104: 0.0246001, 105: 0.0246001, 139: 0.0246001, 102: 0.0246001, 136: 0.0246001, 138: 0.0246001, 182: 0.0246001, 187: 0.0246001, 67: 0.0246001, 69: 0.0246001, 106: 0.0246001, 184: 0.0246001, 185: 0.0246001, 186: 0.0246001, 225: 0.0246001, 33: 0.0246001, 34: 0.0246001, 35: 0.0246001, 36: 0.0246001, 40: 0.0246001, 41: 0.0246001, 42: 0.0246001, 43: 0.0246001, 47: 0.0246001, 48: 0.0246001, 49: 0.0246001, 50: 0.0246001, 51: 0.0246001, 52: 0.0246001, 53: 0.0246001, 54: 0.0246001, 63: 0.0246001, 64: 0.0246001, 65: 0.0246001, 66: 0.0246001, 133: 0.0246001, 135: 0.0246001, 144: 0.0246001, 145: 0.0246001, 140: 0.0246001, 141: 0.0246001, 1198: 2.2273918, 1253: 2.2273918, 1192: 2.2273918, 1193: 2.2273918, 1149: 2.2273918, 1194: 2.2273918, 2: 2.2273918, 1147: 2.2273918, 1150: 2.2273918, 1195: 2.2273918, 1104: 2.2273918, 371: 0.0192851, 372: 0.0192851, 376: 0.0192851, 514: 0.0192851, 515: 0.0192851, 546: 0.0192851, 547: 0.0192851, 416: 0.0192851, 417: 0.0192851, 451: 0.0192851, 452: 0.0192851, 453: 0.0192851, 454: 0.0192851, 457: 0.0192851, 483: 0.0192851, 544: 0.0192851, 545: 0.0192851, 549: 0.0192851, 484: 0.0192851, 486: 0.0192851, 410: 0.0192851, 411: 0.0192851, 412: 0.0192851, 413: 0.0192851, 485: 0.0192851, 513: 0.0192851, 148: 0.0379251, 153: 0.0379251, 196: 0.0379251, 149: 0.0379251, 192: 0.0379251, 193: 0.0379251, 194: 0.0379251, 195: 0.0379251, 236: 0.0379251, 124: 0.0379251, 155: 0.0379251, 114: 0.0379251, 146: 0.0379251, 156: 0.0379251, 161: 0.0379251, 202: 0.0379251, 204: 0.0379251, 207: 0.0379251, 152: 0.0379251, 157: 0.0379251, 118: 0.0379251, 147: 0.0379251, 150: 0.0379251, 151: 0.0379251, 197: 0.0379251, 198: 0.0379251, 199: 0.0379251, 239: 0.0379251, 240: 0.0379251, 241: 0.0379251, 243: 0.0379251, 244: 0.0379251, 245: 0.0379251, 246: 0.0379251, 247: 0.0379251, 250: 0.0379251, 200: 0.0379251, 201: 0.0379251, 203: 0.0379251, 83: 0.0379251, 86: 0.0379251, 112: 0.0379251, 113: 0.0379251, 115: 0.0379251, 637: 0.2623483, 670: 0.2623483, 674: 0.2623483, 675: 0.2623483, 701: 0.2623483, 668: 0.2623483, 669: 0.2623483, 725: 0.2623483, 642: 0.2623483, 672: 0.2623483, 673: 0.2623483, 696: 0.2623483, 697: 0.2623483, 703: 0.2623483, 698: 0.2623483, 699: 0.2623483, 640: 0.2623483, 641: 0.2623483, 643: 0.2623483, 644: 0.2623483, 666: 0.2623483, 671: 0.2623483, 700: 0.2623483, 722: 0.2623483, 749: 0.0380992, 750: 0.0380992, 779: 0.0380992, 780: 0.0380992, 785: 0.0380992, 788: 0.0380992, 724: 0.0380992, 748: 0.0380992, 751: 0.0380992, 715: 0.0380992, 716: 0.0380992, 744: 0.0380992, 745: 0.0380992, 746: 0.0380992, 753: 0.0380992, 758: 0.0380992, 784: 0.0380992, 786: 0.0380992, 787: 0.0380992, 789: 0.0380992, 723: 0.0380992, 752: 0.0380992, 781: 0.0380992, 782: 0.0380992, 710: 0.0380992, 711: 0.0380992, 712: 0.0380992, 754: 0.0380992, 783: 0.0380992, 1711: 0.0758011, 1713: 0.0758011, 1714: 0.0758011, 1480: 0.0758011, 1485: 0.0758011, 1569: 0.0758011, 1570: 0.0758011, 1573: 0.0758011, 1576: 0.0758011, 1571: 0.0758011, 1572: 0.0758011, 1649: 0.0758011, 1654: 0.0758011, 1712: 0.0758011, 1715: 0.0758011, 1716: 0.0758011, 1582: 0.0758011, 1583: 0.0758011, 1651: 0.0758011, 1652: 0.0758011, 1650: 0.0758011, 1717: 0.0758011, 1718: 0.0758011, 1722: 0.0758011, 1579: 0.0758011, 1581: 0.0758011, 1584: 0.0758011, 1648: 0.0758011, 1574: 0.0758011, 1575: 0.0758011, 1577: 0.0758011, 1578: 0.0758011, 1580: 0.0758011, 1647: 0.0758011, 227: 0.0219771, 228: 0.0219771, 229: 0.0219771, 230: 0.0219771, 274: 0.0219771, 275: 0.0219771, 302: 0.0219771, 266: 0.0219771, 267: 0.0219771, 190: 0.0219771, 191: 0.0219771, 231: 0.0219771, 232: 0.0219771, 235: 0.0219771, 242: 0.0219771, 272: 0.0219771, 273: 0.0219771, 276: 0.0219771, 226: 0.0219771, 233: 0.0219771, 234: 0.0219771, 237: 0.0219771, 238: 0.0219771, 268: 0.0219771, 269: 0.0219771, 270: 0.0219771, 271: 0.0219771, 188: 0.0219771, 189: 0.0219771, 985: 0.0358366, 987: 0.0358366, 988: 0.0358366, 1031: 0.0358366, 1032: 0.0358366, 1034: 0.0358366, 1029: 0.0358366, 1030: 0.0358366, 1074: 0.0358366, 1077: 0.0358366, 944: 0.0358366, 947: 0.0358366, 978: 0.0358366, 979: 0.0358366, 981: 0.0358366, 984: 0.0358366, 919: 0.0358366, 953: 0.0358366, 954: 0.0358366, 956: 0.0358366, 957: 0.0358366, 958: 0.0358366, 959: 0.0358366, 993: 0.0358366, 1035: 0.0358366, 1037: 0.0358366, 1038: 0.0358366, 1081: 0.0358366, 1082: 0.0358366, 937: 0.0358366, 938: 0.0358366, 939: 0.0358366, 940: 0.0358366, 941: 0.0358366, 942: 0.0358366, 943: 0.0358366, 973: 0.0358366, 974: 0.0358366, 975: 0.0358366, 977: 0.0358366, 980: 0.0358366, 983: 0.0358366, 1020: 0.0358366, 1023: 0.0358366, 1024: 0.0358366, 948: 0.0358366, 949: 0.0358366, 950: 0.0358366, 951: 0.0358366, 986: 0.0358366, 995: 0.0358366, 1000: 0.0358366, 991: 0.0358366, 994: 0.0358366, 996: 0.0358366, 1027: 0.0358366, 1033: 7.5342434, 1078: 7.5342434, 1025: 0.0358366, 1069: 0.0358366, 1070: 0.0358366, 1073: 0.0358366, 952: 0.0358366, 955: 0.0358366, 989: 0.0358366, 990: 0.0358366, 992: 0.0358366, 1028: 0.0358366, 945: 0.0358366, 946: 0.0358366, 982: 0.0358366, 73: 0.1064836, 74: 0.1064836, 121: 0.1064836, 122: 0.1064836, 154: 0.1064836, 87: 0.1064836, 88: 0.1064836, 89: 0.1064836, 91: 0.1064836, 80: 0.1064836, 81: 0.1064836, 82: 0.1064836, 37: 0.1064836, 38: 0.1064836, 39: 0.1064836, 44: 0.1064836, 85: 0.1064836, 90: 0.1064836, 70: 0.1064836, 71: 0.1064836, 72: 0.1064836, 75: 0.1064836, 0: 0.1064836, 45: 0.1064836, 55: 0.1064836, 56: 0.1064836, 76: 0.1064836, 77: 0.1064836, 119: 0.1064836, 120: 0.1064836, 78: 0.1064836, 79: 0.1064836, 116: 0.1064836, 117: 0.1064836, 690: 0.0766742, 721: 0.0766742, 717: 0.0766742, 718: 0.0766742, 686: 0.0766742, 687: 0.0766742, 691: 0.0766742, 713: 0.0766742, 714: 0.0766742, 695: 0.0766742, 719: 0.0766742, 720: 0.0766742, 747: 0.0766742, 1091: 0.0232039, 1134: 0.0232039, 1041: 0.0232039, 1044: 0.0232039, 1086: 0.0232039, 1089: 0.0232039, 1090: 0.0232039, 1093: 0.0232039, 1184: 0.0232039, 1186: 0.0232039, 1228: 0.0232039, 1231: 0.0232039, 1092: 0.0232039, 1140: 0.0232039, 1141: 0.0232039, 1176: 0.0232039, 1135: 0.0232039, 1136: 0.0232039, 3: 0.0232039, 1188: 0.0232039, 1190: 0.0232039, 1235: 0.0232039, 1236: 0.0232039, 1237: 0.0232039, 1238: 0.0232039, 1239: 0.0232039, 1240: 0.0232039, 1242: 0.0232039, 1294: 0.0232039, 999: 0.0232039, 1036: 0.0232039, 1039: 0.0232039, 1042: 0.0232039, 1003: 0.0232039, 1004: 0.0232039, 1040: 0.0232039, 1043: 0.0232039, 1005: 0.0232039, 1006: 0.0232039, 1007: 0.0232039, 1045: 0.0232039, 1046: 0.0232039, 1047: 0.0232039, 1048: 0.0232039, 1049: 0.0232039, 1050: 0.0232039, 1051: 0.0232039, 1052: 0.0232039, 1144: 0.0232039, 1145: 0.0232039, 1181: 0.0232039, 1183: 0.0232039, 1131: 0.0232039, 1132: 0.0232039, 1137: 0.0232039, 1171: 0.0232039, 1172: 0.0232039, 1173: 0.0232039, 1174: 0.0232039, 1175: 0.0232039, 1178: 0.0232039, 1220: 0.0232039, 1084: 0.0232039, 1127: 0.0232039, 1128: 0.0232039, 1130: 0.0232039, 1133: 0.0232039, 1168: 0.0232039, 961: 0.0232039, 962: 0.0232039, 963: 0.0232039, 964: 0.0232039, 965: 0.0232039, 997: 0.0232039, 998: 0.0232039, 1001: 0.0232039, 1002: 0.0232039, 1083: 0.0232039, 1085: 0.0232039, 1087: 0.0232039, 1088: 0.0232039, 1185: 0.0232039, 1187: 0.0232039, 1189: 0.0232039, 1232: 0.0232039, 1233: 0.0232039, 1234: 0.0232039, 1177: 0.0232039, 1179: 0.0232039, 1180: 0.0232039, 1182: 0.0232039, 1223: 0.0232039, 1224: 0.0232039, 1227: 0.0232039, 1094: 0.0232039, 1095: 0.0232039, 1096: 0.0232039, 1138: 0.0232039, 1139: 0.0232039, 1142: 0.0232039, 1143: 0.0232039, 285: 0.0307537, 288: 0.0307537, 253: 0.0307537, 257: 0.0307537, 206: 0.0307537, 210: 0.0307537, 211: 0.0307537, 248: 0.0307537, 251: 0.0307537, 252: 0.0307537, 304: 0.0307537, 305: 0.0307537, 307: 0.0307537, 308: 0.0307537, 311: 0.0307537, 309: 0.0307537, 277: 0.0307537, 278: 0.0307537, 281: 0.0307537, 291: 0.0307537, 292: 0.0307537, 286: 0.0307537, 289: 0.0307537, 290: 0.0307537, 279: 0.0307537, 280: 0.0307537, 284: 0.0307537, 303: 0.0307537, 306: 0.0307537, 287: 0.0307537, 310: 0.0307537, 249: 0.0307537, 254: 0.0307537, 282: 0.0307537, 283: 0.0307537, 312: 0.0307537, 313: 0.0307537, 525: 0.0462436, 534: 0.0462436, 535: 0.0462436, 539: 0.0462436, 567: 0.0462436, 570: 0.0462436, 526: 0.0462436, 559: 0.0462436, 493: 0.0462436, 496: 0.0462436, 499: 0.0462436, 528: 0.0462436, 529: 0.0462436, 497: 0.0462436, 498: 0.0462436, 503: 0.0462436, 467: 0.0462436, 471: 0.0462436, 472: 0.0462436, 500: 0.0462436, 501: 0.0462436, 504: 0.0462436, 564: 0.0462436, 565: 0.0462436, 560: 0.0462436, 562: 0.0462436, 530: 0.0462436, 531: 0.0462436, 563: 0.0462436, 502: 0.0462436, 507: 0.0462436, 532: 0.0462436, 533: 0.0462436, 536: 0.0462436, 566: 0.0462436, 568: 0.0462436, 569: 0.0462436, 572: 0.0462436, 573: 0.0462436, 494: 0.0462436, 495: 0.0462436, 13: 1.265168, 10: 1.265168, 11: 1.265168, 12: 1.265168, 18: 1.265168, 19: 1.265168, 20: 1.265168, 21: 1.265168, 22: 1.265168, 23: 1.265168, 24: 1.265168, 25: 1.265168, 26: 1.265168, 27: 1.265168, 28: 1.265168, 29: 1.265168, 30: 1.265168, 31: 1.265168, 32: 1.265168, 14: 1.265168, 9: 1.265168, 15: 1.265168, 16: 1.265168, 17: 1.265168, 657: 1.3237872, 659: 1.3237872, 688: 1.3237872, 693: 1.3237872, 658: 1.3237872, 692: 1.3237872, 656: 1.3237872, 694: 1.3237872, 689: 1.3237872, 627: 1.3237872, 92: 0.0417916, 95: 0.0417916, 98: 0.0417916, 125: 0.0417916, 96: 0.0417916, 97: 0.0417916, 99: 0.0417916, 100: 0.0417916, 128: 0.0417916, 94: 0.0417916, 93: 0.0417916, 1204: 0.4186689, 1112: 0.4186689, 1114: 0.4186689, 1117: 0.4186689, 1155: 0.4186689, 1153: 0.4186689, 1205: 0.4186689, 1158: 0.4186689, 1258: 0.4186689, 1203: 0.4186689, 1206: 0.4186689, 1201: 0.4186689, 1157: 0.4186689, 1261: 0.4186689, 1200: 0.4186689, 1156: 0.4186689, 1159: 0.4186689, 762: 0.0677058, 726: 0.0677058, 729: 0.0677058, 728: 0.0677058, 755: 0.0677058, 727: 0.0677058, 730: 0.0677058, 731: 0.0677058, 736: 0.0677058, 756: 0.0677058, 757: 0.0677058, 759: 0.0677058, 760: 0.0677058, 761: 0.0677058, 763: 0.0677058, 765: 0.0677058, 766: 0.0677058, 732: 0.0677058, 405: 0.0193792, 406: 0.0193792, 407: 0.0193792, 408: 0.0193792, 409: 0.0193792, 445: 0.0193792, 446: 0.0193792, 319: 0.0193792, 320: 0.0193792, 321: 0.0193792, 322: 0.0193792, 323: 0.0193792, 324: 0.0193792, 325: 0.0193792, 333: 0.0193792, 334: 0.0193792, 337: 0.0193792, 473: 0.0193792, 474: 0.0193792, 342: 0.0193792, 362: 0.0193792, 364: 0.0193792, 365: 0.0193792, 367: 0.0193792, 368: 0.0193792, 438: 0.0193792, 441: 0.0193792, 442: 0.0193792, 443: 0.0193792, 444: 0.0193792, 448: 0.0193792, 338: 0.0193792, 339: 0.0193792, 340: 0.0193792, 341: 0.0193792, 343: 0.0193792, 360: 0.0193792, 361: 0.0193792, 366: 0.0193792, 369: 0.0193792, 370: 0.0193792, 399: 0.0193792, 400: 0.0193792, 401: 0.0193792, 403: 0.0193792, 404: 0.0193792, 930: 0.0975902, 1056: 0.0975902, 1099: 0.0975902, 1100: 0.0975902, 1105: 0.0975902, 1013: 0.0975902, 1014: 0.0975902, 1057: 0.0975902, 1058: 0.0975902, 1059: 0.0975902, 1101: 0.0975902, 1146: 0.0975902, 972: 0.0975902, 931: 0.0975902, 1010: 0.0975902, 966: 0.0975902, 969: 0.0975902, 970: 0.0975902, 971: 0.0975902, 976: 0.0975902, 1008: 0.0975902, 1009: 0.0975902, 1011: 0.0975902, 1103: 0.0975902, 934: 0.0975902, 935: 0.0975902, 1055: 0.0975902, 1060: 0.0975902, 1053: 0.0975902, 1054: 0.0975902, 1097: 0.0975902, 1102: 0.0975902, 896: 0.0975902, 1098: 0.0975902, 968: 0.0975902, 967: 0.0975902, 1207: 0.065074, 1209: 0.065074, 1266: 0.065074, 1214: 0.065074, 1269: 0.065074, 1265: 0.065074, 1267: 0.065074, 1272: 0.065074, 1351: 0.065074, 1354: 0.065074, 1358: 0.065074, 1274: 0.065074, 1276: 0.065074, 1221: 0.065074, 1275: 0.065074, 1277: 0.065074, 1278: 0.065074, 1279: 0.065074, 1280: 0.065074, 1359: 0.065074, 1362: 0.065074, 1210: 0.065074, 1355: 0.065074, 1356: 0.065074, 1357: 0.065074, 1361: 0.065074, 1212: 0.065074, 1213: 0.065074, 1215: 0.065074, 1216: 0.065074, 1217: 0.065074, 1218: 0.065074, 1219: 0.065074, 1222: 0.065074, 1270: 0.065074, 1273: 0.065074, 1: 0.0301448, 584: 0.0301448, 580: 0.0301448, 578: 0.0301448, 579: 0.0301448, 581: 0.0301448, 548: 0.0301448, 550: 0.0301448, 551: 0.0301448, 552: 0.0301448, 553: 0.0301448, 554: 0.0301448, 557: 0.0301448, 1151: 7.5342434, 1152: 7.5342434, 1199: 7.5342434, 1154: 7.5342434, 1196: 7.5342434, 1257: 7.5342434, 1061: 0.0562116, 1062: 0.0562116, 1063: 0.0562116, 1202: 7.5342434, 1197: 7.5342434, 1254: 7.5342434, 475: 0.0176787, 476: 0.0176787, 479: 0.0176787, 505: 0.0176787, 508: 0.0176787, 509: 0.0176787, 506: 0.0176787, 510: 0.0176787, 511: 0.0176787, 537: 0.0176787, 538: 0.0176787, 540: 0.0176787, 541: 0.0176787, 542: 0.0176787, 543: 0.0176787, 571: 0.0176787, 574: 0.0176787, 575: 0.0176787, 576: 0.0176787, 577: 0.0176787, 447: 0.0176787, 449: 0.0176787, 450: 0.0176787, 477: 0.0176787, 478: 0.0176787, 480: 0.0176787, 481: 0.0176787, 482: 0.0176787, 923: 0.0343723, 925: 0.0343723, 849: 0.0343723, 888: 0.0343723, 891: 0.0343723, 921: 0.0343723, 922: 0.0343723, 924: 0.0343723, 844: 0.0343723, 886: 0.0343723, 840: 0.0343723, 842: 0.0343723, 845: 0.0343723, 890: 0.0343723, 887: 0.0343723, 889: 0.0343723, 926: 0.0343723, 927: 0.0343723, 928: 0.0343723, 929: 0.0343723, 960: 0.0343723, 623: 0.0311132, 652: 0.0311132, 645: 0.0311132, 646: 0.0311132, 647: 0.0311132, 650: 0.0311132, 651: 0.0311132, 676: 0.0311132, 677: 0.0311132, 680: 0.0311132, 681: 0.0311132, 621: 0.0311132, 648: 0.0311132, 649: 0.0311132, 619: 0.0311132, 620: 0.0311132, 622: 0.0311132, 624: 0.0311132, 678: 0.0311132, 679: 0.0311132, 683: 0.0311132, 708: 0.0311132, 709: 0.0311132, 654: 0.0311132, 655: 0.0311132, 682: 0.0311132, 684: 0.0311132, 685: 0.0311132, 653: 0.0311132, 1292: 0.0149091, 1371: 0.0149091, 1372: 0.0149091, 1374: 0.0149091, 1377: 0.0149091, 1386: 0.0149091, 1387: 0.0149091, 1388: 0.0149091, 1389: 0.0149091, 1393: 0.0149091, 1490: 0.0149091, 1491: 0.0149091, 1492: 0.0149091, 1380: 0.0149091, 1382: 0.0149091, 1383: 0.0149091, 1385: 0.0149091, 1381: 0.0149091, 1479: 0.0149091, 1482: 0.0149091, 1290: 0.0149091, 1291: 0.0149091, 1293: 0.0149091, 1295: 0.0149091, 1296: 0.0149091, 1378: 0.0149091, 1379: 0.0149091, 1483: 0.0149091, 1484: 0.0149091, 1486: 0.0149091, 1489: 0.0149091, 1384: 0.0149091, 1487: 0.0149091, 1488: 0.0149091, 1493: 0.0149091, 1375: 0.0149091, 1376: 0.0149091, 1241: 0.0149091, 1243: 0.0149091, 1245: 0.0149091, 1297: 0.0149091, 1298: 0.0149091, 1299: 0.0149091, 1300: 0.0149091, 1301: 0.0149091, 1304: 0.0149091, 1244: 0.0149091, 1302: 0.0149091, 1303: 0.0149091, 1305: 0.0149091, 1308: 0.0149091, 1390: 0.0149091, 314: 0.0557891, 329: 0.0557891, 316: 0.0557891, 317: 0.0557891, 330: 0.0557891, 326: 0.0557891, 218: 0.0557891, 221: 0.0557891, 327: 0.0557891, 328: 0.0557891, 351: 0.0557891, 297: 0.0557891, 298: 0.0557891, 299: 0.0557891, 300: 0.0557891, 301: 0.0557891, 318: 0.0557891, 220: 0.0557891, 222: 0.0557891, 223: 0.0557891, 224: 0.0557891, 260: 0.0557891, 263: 0.0557891, 264: 0.0557891, 265: 0.0557891, 258: 0.0557891, 293: 0.0557891, 294: 0.0557891, 295: 0.0557891, 296: 0.0557891, 315: 0.0557891, 332: 0.0557891, 259: 0.0557891, 261: 0.0557891, 262: 0.0557891, 1064: 0.0562116, 1106: 0.0562116, 1107: 0.0562116, 1109: 0.0562116, 1110: 0.0562116, 1022: 0.0562116, 1012: 0.0562116, 1015: 0.0562116, 1016: 0.0562116, 1017: 0.0562116, 1018: 0.0562116, 1065: 0.0562116, 1108: 0.0562116, 1113: 0.0562116, 1148: 0.0562116, 1067: 0.0562116, 1068: 0.0562116, 1111: 0.0562116}
prefecture_tile_dict = {'Aichi': [895, 865, 823, 
                                      866, 821, 825, 897, 46, 57, 58, 59, 60, 61, 62, 864, 869,
                                        862, 858, 859, 860, 818, 512, 824, 820, 861, 898, 899, 900, 932, 933, 936, 819, 402, 433, 434, 437, 516, 517, 518, 519, 523, 863, 822], 'Akita': [1512, 1513, 1517, 1605, 1601, 1602, 1603, 1604, 1607, 1608, 1672, 1675, 1400, 1499, 1502, 1503, 1505, 1506, 1313, 1314, 1317, 1399, 1402, 1403, 1404, 1405, 1408, 1409, 1413, 1507, 1510, 1511, 1514, 1312, 1315, 1310, 1394, 1395, 1396, 1397, 1398, 1401, 1392, 1494, 1495, 1496, 1497, 1498, 1585, 1586, 1504, 1508, 1509, 1593, 1594, 1595, 1596, 1597, 1598, 1600, 1500, 1501, 1589, 1590, 1306, 1307, 1309, 1311, 1391, 1316, 1318, 1320, 1406, 1407, 1410, 1411], 'Aomori': [1520, 1609, 1612, 1744, 1745, 1746, 1791, 1618, 1622, 1685, 1687, 1688, 1689, 1690, 1691, 1692, 1747, 1748, 1749, 1750, 1676, 1677, 1679, 1680, 1681, 1682, 1686, 1740, 1743, 1319, 1414, 1415, 1416, 1418, 1419, 1420, 1421, 1422, 1519, 1522, 1523, 1526, 1527, 1524, 1525, 1528, 1529, 1610, 1611, 1613, 1614, 1615, 1616, 1617, 1683, 1684, 1516, 1521, 1606, 1412, 1417, 1515, 1518], 'Chiba': [1260, 1246, 1248, 1336, 1341, 1446, 1271, 1345, 1337, 1338, 1259, 1342, 1251, 1249, 1250, 1252, 1255, 1340, 1256, 1335, 1334, 1552, 1449, 1247, 1339, 1445], 'Ehime': [460, 461, 487, 488, 489, 490, 347, 377, 418, 419, 420, 421, 422, 425, 455, 456, 458, 459, 378, 379, 381, 415, 423, 424, 426, 346, 348, 349, 350, 382, 383, 384, 386, 387, 344, 345, 373, 374, 375, 380, 414], 'Fukui': [735, 737, 739, 764, 767, 702, 704, 705, 706, 707, 733, 734, 797, 798, 799, 801, 802, 803, 804, 834, 835, 743, 771, 774, 775, 738, 740, 768, 769, 770, 741, 742, 772, 773], 'Fukuoka': [162, 165, 158, 213, 215, 160, 123, 214, 256, 255, 127, 163, 171, 216, 217, 219, 166, 172, 131, 167, 1262, 170, 205, 208, 209, 168, 164, 169, 212, 159, 126, 129, 130, 132], 'Fukushima': [1475, 1476, 1478, 1368, 1369, 1470, 1467, 1468, 1469, 1567, 1646, 1556, 1557, 1559, 1560, 1472, 1473, 1558, 1561, 1562, 1564, 1360, 1363, 1364, 1365, 1366, 1463, 1466, 1474, 1477, 1563, 1568, 1643, 1644, 1645, 1328, 1329, 1330, 1331, 1332, 1333, 1435, 1437, 1438, 1439, 1440, 1441, 1442, 1443, 1444, 1481, 1539, 1540, 1541, 1542, 1543, 1544, 1565, 1566, 1630, 1631, 1632, 1633, 1636, 1695, 1696, 1699, 1225, 1226, 1229, 1230, 1281, 1282, 1283, 1284, 1285, 1286, 1287, 1288, 1289, 1367, 1370, 1373, 1471], 'Gifu': [790, 791, 793, 878, 880, 881, 913, 914, 915, 916, 917, 920, 867, 829, 903, 907, 908, 912, 828, 868, 901, 871, 872, 873, 870, 826, 827, 836, 841, 879, 882, 883, 884, 885, 918, 794, 795, 796, 800, 830, 831, 832, 833, 837, 874, 875, 876, 877, 909, 910, 911, 902, 904, 905, 906, 792], 'Gunma': [1208, 1211, 1162, 1079, 1122, 1123, 1124, 1125, 1126, 1129, 1163, 1164, 1165, 1167, 1169, 1170, 1116, 1121, 1120, 1075, 1080, 1119, 1071, 1072, 1076, 1115, 1118, 1160, 1161, 1166], 'Hiroshima': [462, 388, 389, 390, 391, 464, 431, 432, 463, 465, 468, 402, 433, 434, 437, 516, 517, 518, 519, 523, 863, 435, 436, 439, 440, 466, 469, 470, 331, 336, 353, 427, 428, 429, 393, 394, 430, 335, 356, 357, 358, 359, 363, 392, 395, 396, 397, 398, 352, 354, 355, 385], 'Hokkaido': [1619, 1620, 1621, 1624, 1628, 1693, 1694, 1545, 1546, 1547, 1548, 1549, 1550, 1551, 1634, 1635, 1637, 1638, 1639, 1640, 1641, 1642, 1700, 1701, 1703, 1704, 1705, 1706, 1902, 1905, 1906, 1907, 1946, 1947, 1948, 1950, 1951, 1952, 1953, 1990, 1991, 1993, 1994, 1996, 1627, 1629, 1928, 1929, 1932, 1933, 1937, 1969, 1970, 1971, 1972, 1973, 1974, 1975, 1976, 1977, 1978, 1979, 1980, 1981, 1983, 1984, 1988, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025, 2026, 2027, 2028, 2029, 2030, 2033, 2046, 2047, 2048, 2049, 2050, 2051, 2052, 2053, 2054, 2055, 2056, 2058, 2071, 2072, 2074, 2075, 1842, 1843, 1844, 1845, 1847, 1848, 1885, 1886, 1887, 1888, 1889, 1890, 1891, 1892, 1893, 1927, 1930, 1931, 1934, 1799, 1804, 2108, 2109, 2110, 2111, 2112, 2121, 2122, 2123, 2124, 2125, 2126, 2127, 2128, 2136, 2137, 2138, 2139, 2140, 2141, 2142, 2143, 2151, 2154, 2155, 2156, 2158, 2159, 2160, 2161, 2168, 2170, 1765, 1766, 1768, 1769, 1770, 1806, 1809, 1810, 1811, 1812, 1813, 1814, 1815, 1816, 1817, 1818, 1819, 1821, 1858, 1861, 1862, 1865, 1752, 1839, 1884, 1707, 1708, 1709, 1710, 1820, 1822, 1823, 1824, 1825, 1826, 1827, 1828, 1829, 1830, 1831, 1870, 1873, 1874, 1875, 1876, 1877, 1878, 1879, 1880, 1881, 1882, 1883, 1921, 1924, 1925, 1926, 1802, 1803, 1897, 1900, 1903, 1759, 1760, 1798, 1801, 1856, 1995, 1999, 2000, 2003, 2004, 2007, 2031, 2032, 2034, 2035, 2036, 2037, 2038, 2039, 2040, 2041, 2042, 2043, 2044, 2045, 2064, 2067, 2068, 2069, 2070, 2091, 1846, 1849, 1852, 2145, 2148, 2149, 2150, 2152, 2153, 2157, 2162, 2163, 2164, 2165, 2166, 2167, 2169, 2171, 2172, 2173, 2174, 2175, 2176, 2177, 2178, 2179, 2180, 2181, 2182, 2183, 2184, 2185, 2186, 2187, 1793, 1795, 1796, 1840, 1841, 1807, 1853, 1854, 1805, 1808, 1850, 1851, 1855, 1857, 1859, 1860, 1864, 1901, 1904, 1894, 1895, 1896, 1898, 1899, 1935, 1936, 1938, 1939, 1940, 1941, 1942, 1943, 1944, 1945, 1949, 1982, 1985, 1986, 1987, 1989, 1992, 1697, 1698, 1702, 1751, 1753, 1755, 1756, 1794, 1328, 1329, 1330, 1331, 1332, 1333, 1435, 1437, 1438, 1439, 1440, 1441, 1442, 1443, 1444, 1481, 1539, 1540, 1541, 1542, 1543, 1544, 1565, 1566, 1630, 1631, 1632, 1633, 1636, 1695, 1696, 1699, 1797, 1800, 1754, 1757, 1758, 1761, 1762, 1763, 1764, 1767, 4, 2073, 2076, 2077, 2094, 2095, 2096, 2097, 2098, 2101, 2113, 2114, 2115, 2116, 2117, 2118, 2119, 2120, 2129, 2130, 2131, 2132, 2133, 2134, 2135, 2144, 2146, 2147, 1019, 1021, 1026, 1066, 1191, 1321, 1322, 1323, 1324, 1325, 1326, 1327, 1423, 1424, 1425, 1426, 1427, 1428, 1429, 1430, 1431, 1432, 1433, 1434, 1436, 1530, 1531, 1532, 1533, 1534, 1535, 1536, 1537, 1538, 1623, 1625, 1626, 2057, 2059, 2060, 2061, 2062, 2063, 2065, 2066, 2078, 2079, 2080, 2081, 2082, 2083, 2084, 2085, 2086, 2087, 2088, 2089, 2090, 2092, 2093, 2099, 2100, 2102, 2103, 2104, 2105, 2106, 2107, 1863, 1866, 1867, 1868, 1869, 1871, 1872, 1908, 1909, 1910, 1911, 1912, 1913, 1914, 1915, 1916, 1917, 1918, 1919, 1920, 1922, 1923, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966, 1967, 1968, 1997, 1998, 2001, 2002, 2005, 2006], 'Hyogo': [602, 605, 663, 628, 660, 662, 585, 595, 614, 615, 616, 617, 618, 639, 603, 604, 661, 629, 630, 667, 634, 664, 607, 608, 633, 665, 591, 593, 594, 596, 609, 610, 613, 635, 638, 597, 598, 599, 611, 612, 636, 600, 625, 626, 586, 587, 588, 589, 590, 592, 606, 632, 601, 631], 'Ibaraki': [1349, 1344, 1263, 1460, 1461, 1465, 1464, 1554, 1555, 1343, 1347, 1456, 1457, 1448, 1458, 1459, 1462, 1264, 1447, 1450, 1268, 1348, 1553, 1453, 131, 167, 1262, 1350, 1452, 1352, 1353, 1455, 1346, 1451, 1454], 'Ishikawa': [812, 839, 848, 853, 805, 806, 893, 894, 813, 816, 846, 847, 850, 811, 814, 843, 809, 810, 807, 808, 838, 776, 777, 778, 815, 817, 851, 852, 854, 855, 856, 857, 892], 'Iwate': [1776, 1777, 1832, 1833, 1773, 1721, 1771, 1772, 1592, 1659, 1662, 1723, 1780, 1781, 1782, 1785, 1834, 1835, 1836, 1837, 1599, 1668, 1669, 1671, 1674, 1732, 1733, 1588, 1653, 1655, 1658, 1719, 1725, 1726, 1729, 1730, 1774, 1775, 1778, 1779, 1591, 1660, 1661, 1663, 1666, 1724, 1727, 1673, 1678, 1735, 1736, 1737, 1738, 1739, 1741, 1742, 1587, 1656, 1657, 1720, 1783, 1784, 1786, 1787, 1788, 1789, 1790, 1792, 1838, 1664, 1665, 1667, 1670, 1728, 1731, 1734], 'Kagawa': [524, 522, 527, 521, 555, 556, 558, 561, 582, 583, 492, 491, 520], 'Kagoshima': [178, 179, 180, 183, 68, 84, 107, 108, 110, 111, 109, 142, 143, 134, 177, 101, 103, 5, 6, 7, 8, 173, 174, 175, 176, 137, 181, 104, 105, 139, 102, 136, 138, 182, 187, 67, 69, 106, 184, 185, 186, 225, 33, 34, 35, 36, 40, 41, 42, 43, 47, 48, 49, 50, 51, 52, 53, 54, 63, 64, 65, 66, 133, 135, 144, 145, 140, 141], 'Kanagawa': [1198, 1253, 1192, 1193, 1149, 1194, 2, 1147, 1150, 1195, 1104], 'Kochi': [371, 372, 376, 514, 515, 546, 547, 416, 417, 451, 452, 453, 454, 457, 483, 544, 545, 549, 484, 486, 410, 411, 412, 413, 485, 513, 512], 'Kumamoto': [148, 153, 196, 149, 192, 193, 194, 195, 236, 124, 155, 114, 146, 156, 161, 202, 204, 207, 152, 157, 118, 147, 150, 151, 197, 198, 199, 239, 240, 241, 243, 244, 245, 246, 247, 250, 200, 201, 203, 83, 86, 112, 113, 115], 'Kyoto': [637, 670, 674, 675, 701, 668, 669, 725, 642, 672, 673, 696, 697, 703, 698, 699, 640, 641, 643, 644, 666, 671, 700, 722], 'Mie': [749, 750, 779, 780, 785, 788, 724, 748, 751, 715, 716, 744, 745, 746, 753, 758, 784, 786, 787, 789, 723, 752, 781, 782, 710, 711, 712, 754, 783], 'Miyagi': [1711, 1713, 1714, 1480, 1485, 1569, 1570, 1573, 1576, 1571, 1572, 1649, 1654, 1712, 1715, 1716, 1582, 1583, 1651, 1652, 1650, 1717, 1718, 1722, 1579, 1581, 1584, 1648, 1574, 1575, 1577, 1578, 1580, 1647], 'Miyazaki': [227, 228, 229, 230, 274, 275, 302, 266, 267, 190, 191, 231, 232, 235, 242, 272, 273, 276, 226, 233, 234, 237, 238, 268, 269, 270, 271, 188, 189], 'Nagano': [985, 987, 988, 1031, 1032, 1034, 1029, 1030, 1074, 1077, 944, 947, 978, 979, 981, 984, 919, 953, 954, 956, 957, 958, 959, 993, 1035, 1037, 1038, 1081, 1082, 937, 938, 939, 940, 941, 942, 943, 973, 974, 975, 977, 980, 983, 1020, 1023, 1024, 948, 949, 950, 951, 986, 995, 1000, 991, 994, 996, 1027, 1033, 1078, 1025, 1069, 1070, 1073, 952, 955, 989, 990, 992, 1028, 945, 946, 982], 'Nagasaki': [73, 74, 121, 122, 154, 87, 88, 89, 91, 46, 57, 58, 59, 60, 61, 62, 80, 81, 82, 37, 38, 39, 44, 85, 90, 70, 71, 72, 75, 0, 45, 55, 56, 76, 77, 119, 120, 78, 79, 116, 117], 'Nara': [690, 721, 717, 718, 686, 687, 691, 713, 714, 695, 719, 720, 747], 'Niigata': [1091, 1134, 1041, 1044, 1086, 1089, 1090, 1093, 1184, 1186, 1228, 1231, 1092, 1140, 1141, 1176, 1135, 1136, 3, 1188, 1190, 1235, 1236, 1237, 1238, 1239, 1240, 1242, 1294, 999, 1036, 1039, 1042, 1003, 1004, 1040, 1043, 1005, 1006, 1007, 1045, 1046, 1047, 1048, 1049, 1050, 1051, 1052, 1144, 1145, 1181, 1183, 1131, 1132, 1137, 1171, 1172, 1173, 1174, 1175, 1178, 1220, 1084, 1127, 1128, 1130, 1133, 1168, 961, 962, 963, 964, 965, 997, 998, 1001, 1002, 1083, 1085, 1087, 1088, 1185, 1187, 1189, 1232, 1233, 1234, 1177, 1179, 1180, 1182, 1223, 1224, 1227, 1094, 1095, 1096, 1138, 1139, 1142, 1143], 'Oita': [285, 288, 253, 257, 206, 210, 211, 248, 251, 252, 304, 305, 307, 308, 311, 309, 277, 278, 281, 291, 292, 286, 289, 290, 279, 280, 284, 303, 306, 287, 310, 249, 254, 282, 283, 312, 313], 'Okayama': [525, 534, 535, 539, 567, 570, 526, 559, 493, 496, 499, 528, 529, 497, 498, 503, 467, 471, 472, 500, 501, 504, 564, 565, 560, 562, 530, 531, 563, 502, 507, 532, 533, 536, 566, 568, 569, 572, 573, 494, 495], 'Okinawa': [13, 10, 11, 12, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 14, 9, 15, 16, 17], 'Osaka': [741, 742, 772, 773, 657, 659, 688, 109, 142, 143, 693, 658, 692, 656, 694, 689, 627], 'Saga': [92, 95, 98, 125, 96, 97, 99, 100, 128, 94, 93], 'Saitama': [1204, 1112, 1114, 1117, 1155, 1153, 1205, 1158, 1258, 1203, 1206, 1201, 1157, 1261, 1200, 1156, 1159], 'Shiga': [762, 726, 729, 728, 755, 727, 730, 731, 736, 756, 757, 759, 760, 761, 763, 765, 766, 732], 'Shimane': [405, 406, 407, 408, 409, 445, 446, 319, 320, 321, 322, 323, 324, 325, 333, 334, 337, 473, 474, 342, 362, 364, 365, 367, 368, 438, 441, 442, 443, 444, 448, 338, 339, 340, 341, 343, 360, 361, 366, 369, 370, 399, 400, 401, 403, 404], 'Shizuoka': [930, 1056, 1099, 1100, 1105, 1013, 1014, 1057, 1058, 1059, 1101, 1146, 972, 931, 1010, 966, 969, 970, 971, 976, 1008, 1009, 1011, 1103, 934, 935, 1055, 1060, 1053, 1054, 1097, 1102, 896, 1098, 968, 967], 'Tochigi': [1207, 1209, 1266, 1214, 1269, 1265, 1267, 1272, 1351, 1354, 1358, 1274, 1276, 1221, 1275, 1277, 1278, 1279, 1280, 1359, 1362, 1210, 1271, 1345, 1355, 1356, 1357, 1361, 1212, 1213, 1215, 1216, 1217, 1218, 1219, 1222, 1270, 1273], 'Tokushima': [1, 584, 580, 578, 579, 581, 548, 550, 551, 552, 553, 554, 557, 402, 433, 434, 437, 516, 517, 518, 519, 523, 863], 'Tokyo': [1151, 1152, 463, 465, 468, 1199, 1154, 1196, 1257, 1061, 1062, 1063, 1033, 1078, 1202, 1162, 1197, 1254], 'Tottori': [475, 476, 479, 505, 508, 509, 506, 510, 511, 537, 538, 540, 541, 542, 543, 571, 574, 575, 576, 577, 447, 449, 450, 477, 478, 480, 481, 482], 'Toyama': [923, 925, 849, 888, 891, 921, 922, 924, 844, 886, 840, 842, 845, 890, 887, 889, 926, 927, 928, 929, 960], 'Wakayama': [623, 652, 645, 646, 647, 650, 651, 676, 677, 680, 681, 621, 648, 649, 619, 620, 622, 624, 678, 679, 683, 708, 709, 654, 655, 682, 684, 685, 653], 'Yamagata': [1292, 1371, 1372, 1374, 1377, 1386, 1387, 1388, 1389, 1393, 1490, 1491, 1492, 1380, 1382, 1383, 1385, 1381, 1479, 1482, 1290, 1291, 1293, 1295, 1296, 1378, 1379, 1483, 1484, 1486, 1489, 1384, 1487, 1488, 1493, 1375, 1376, 1241, 1243, 1245, 1297, 1298, 1299, 1300, 1301, 1304, 1244, 1302, 1303, 1305, 1308, 1390], 'Yamaguchi': [314, 329, 316, 317, 330, 326, 218, 221, 327, 328, 351, 297, 298, 299, 300, 301, 318, 220, 222, 223, 224, 260, 263, 264, 265, 258, 293, 294, 295, 296, 315, 332, 259, 261, 262], 'Yamanashi': [1064, 1106, 1107, 1109, 1110, 1022, 1012, 1015, 1016, 1017, 1018, 1065, 1019, 1021, 1026, 1066, 1191, 1321, 1322, 1323, 1324, 1325, 1326, 1327, 1423, 1424, 1425, 1426, 1427, 1428, 1429, 1430, 1431, 1432, 1433, 1434, 1436, 1530, 1531, 1532, 1533, 1534, 1535, 1536, 1537, 1538, 1623, 1625, 1626, 1108, 1113, 1148, 1067, 1068, 1111, 1061, 1062, 1063]}

# Container for data
data_to_dump = {'prefecture_city_list': prefecture_city_list, 'prefecture_area_dict': prefecture_area_dict,
                'prefecture_pop_dict': prefecture_pop_dict, 'tile_pdf_dict': tile_pdf_dict, 'prefecture_tile_dict': prefecture_tile_dict}
with open('./population/relevant_data/pickleFiles/pickledData.pkl', 'wb') as file:
      data_list = pickle.dump(data_to_dump,file)







  