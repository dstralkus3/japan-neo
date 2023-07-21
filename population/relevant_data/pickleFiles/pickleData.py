
import pickle

# Data sets recovered from the functions within scraping.py and data_manipulation.py
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
prefecture_pop_dict = {'Akita': 634, 'Aomori': 1528, 'Fukushima': 1036, 'Iwate': 693, 'Miyagi': 2306, 'Yamagata': 580, 'Chiba': 8363, 'Gunma': 1746, 'Ibaraki': 2623, 'Kanagawa': 22479, 'Saitama': 6642, 'Tochigi': 1742, 'Tokyo': 68958, 'Aichi': 7736, 'Fukui': 601, 'Gifu': 1274, 'Ishikawa': 1031, 'Nagano': 2030, 'Niigata': 1219, 'Shizuoka': 3170, 'Toyama': 609, 'Yamanashi': 1048, 'Kyoto': 5054, 'Mie': 919, 'Nara': 1182, 'Osaka': 10535, 'Shiga': 1136, 'Wakayama': 614, 'Hiroshima': 2602, 'Okayama': 1374, 'Shimane': 543, 'Tottori': 259, 'Yamaguchi': 1424, 'Ehime': 634, 'Kagawa': 647, 'Tokushima': 522, 'Fukuoka': 4779, 'Kagoshima': 944, 'Kumamoto': 1173, 'Miyazaki': 710, 'Nagasaki': 1838, 'Okinawa': 12056, 'Saga': 426, 'Hokkaido': 4553, 'Hyogo': 6621, 'Kochi': 572, 'Oita': 814}
tile_pdf_dict ={895: 179.9069767, 865: 179.9069767, 823: 179.9069767, 866: 179.9069767, 821: 179.9069767, 825: 179.9069767, 897: 179.9069767, 46: 44.8292683, 57: 44.8292683, 58: 44.8292683, 59: 44.8292683, 60: 44.8292683, 61: 44.8292683, 62: 44.8292683, 864: 179.9069767, 869: 179.9069767, 862: 179.9069767, 858: 179.9069767, 859: 179.9069767, 860: 179.9069767, 818: 179.9069767, 512: 21.1851852, 824: 179.9069767, 820: 179.9069767, 861: 179.9069767, 898: 179.9069767, 899: 179.9069767, 900: 179.9069767, 932: 179.9069767, 933: 179.9069767, 936: 179.9069767, 819: 179.9069767, 402: 22.6956522, 433: 22.6956522, 434: 22.6956522, 437: 22.6956522, 516: 22.6956522, 517: 22.6956522, 518: 22.6956522, 519: 22.6956522, 523: 22.6956522, 863: 22.6956522, 822: 179.9069767, 1512: 8.3421053, 1513: 8.3421053, 1517: 8.3421053, 1605: 8.3421053, 1601: 8.3421053, 1602: 8.3421053, 1603: 8.3421053, 1604: 8.3421053, 1607: 8.3421053, 1608: 8.3421053, 1672: 8.3421053, 1675: 8.3421053, 1400: 8.3421053, 1499: 8.3421053, 1502: 8.3421053, 1503: 8.3421053, 1505: 8.3421053, 1506: 8.3421053, 1313: 8.3421053, 1314: 8.3421053, 1317: 8.3421053, 1399: 8.3421053, 1402: 8.3421053, 1403: 8.3421053, 1404: 8.3421053, 1405: 8.3421053, 1408: 8.3421053, 1409: 8.3421053, 1413: 8.3421053, 1507: 8.3421053, 1510: 8.3421053, 1511: 8.3421053, 1514: 8.3421053, 1312: 8.3421053, 1315: 8.3421053, 1310: 8.3421053, 1394: 8.3421053, 1395: 8.3421053, 1396: 8.3421053, 1397: 8.3421053, 1398: 8.3421053, 1401: 8.3421053, 1392: 8.3421053, 1494: 8.3421053, 1495: 8.3421053, 1496: 8.3421053, 1497: 8.3421053, 1498: 8.3421053, 1585: 8.3421053, 1586: 8.3421053, 1504: 8.3421053, 1508: 8.3421053, 1509: 8.3421053, 1593: 8.3421053, 1594: 8.3421053, 1595: 8.3421053, 1596: 8.3421053, 1597: 8.3421053, 1598: 8.3421053, 1600: 8.3421053, 1500: 8.3421053, 1501: 8.3421053, 1589: 8.3421053, 1590: 8.3421053, 1306: 8.3421053, 1307: 8.3421053, 1309: 8.3421053, 1311: 8.3421053, 1391: 8.3421053, 1316: 8.3421053, 1318: 8.3421053, 1320: 8.3421053, 1406: 8.3421053, 1407: 8.3421053, 1410: 8.3421053, 1411: 8.3421053, 1520: 24.2539683, 1609: 24.2539683, 1612: 24.2539683, 1744: 24.2539683, 1745: 24.2539683, 1746: 24.2539683, 1791: 24.2539683, 1618: 24.2539683, 1622: 24.2539683, 1685: 24.2539683, 1687: 24.2539683, 1688: 24.2539683, 1689: 24.2539683, 1690: 24.2539683, 1691: 24.2539683, 1692: 24.2539683, 1747: 24.2539683, 1748: 24.2539683, 1749: 24.2539683, 1750: 24.2539683, 1676: 24.2539683, 1677: 24.2539683, 1679: 24.2539683, 1680: 24.2539683, 1681: 24.2539683, 1682: 24.2539683, 1686: 24.2539683, 1740: 24.2539683, 1743: 24.2539683, 1319: 24.2539683, 1414: 24.2539683, 1415: 24.2539683, 1416: 24.2539683, 1418: 24.2539683, 1419: 24.2539683, 1420: 24.2539683, 1421: 24.2539683, 1422: 24.2539683, 1519: 24.2539683, 1522: 24.2539683, 1523: 24.2539683, 1526: 24.2539683, 1527: 24.2539683, 1524: 24.2539683, 1525: 24.2539683, 1528: 24.2539683, 1529: 24.2539683, 1610: 24.2539683, 1611: 24.2539683, 1613: 24.2539683, 1614: 24.2539683, 1615: 24.2539683, 1616: 24.2539683, 1617: 24.2539683, 1683: 24.2539683, 1684: 24.2539683, 1516: 24.2539683, 1521: 24.2539683, 1606: 24.2539683, 1412: 24.2539683, 1417: 24.2539683, 1515: 24.2539683, 1518: 24.2539683, 1260: 321.6538462, 1246: 321.6538462, 1248: 321.6538462, 1336: 321.6538462, 1341: 321.6538462, 1446: 321.6538462, 1271: 45.8421053, 1345: 45.8421053, 1337: 321.6538462, 1338: 321.6538462, 1259: 321.6538462, 1342: 321.6538462, 1251: 321.6538462, 1249: 321.6538462, 1250: 321.6538462, 1252: 321.6538462, 1255: 321.6538462, 1340: 321.6538462, 1256: 321.6538462, 1335: 321.6538462, 1334: 321.6538462, 1552: 321.6538462, 1449: 321.6538462, 1247: 321.6538462, 1339: 321.6538462, 1445: 321.6538462, 460: 15.4634146, 461: 15.4634146, 487: 15.4634146, 488: 15.4634146, 489: 15.4634146, 490: 15.4634146, 347: 15.4634146, 377: 15.4634146, 418: 15.4634146, 419: 15.4634146, 420: 15.4634146, 421: 15.4634146, 422: 15.4634146, 425: 15.4634146, 455: 15.4634146, 456: 15.4634146, 458: 15.4634146, 459: 15.4634146, 378: 15.4634146, 379: 15.4634146, 381: 15.4634146, 415: 15.4634146, 423: 15.4634146, 424: 15.4634146, 426: 15.4634146, 346: 15.4634146, 348: 15.4634146, 349: 15.4634146, 350: 15.4634146, 382: 15.4634146, 383: 15.4634146, 384: 15.4634146, 386: 15.4634146, 387: 15.4634146, 344: 15.4634146, 345: 15.4634146, 373: 15.4634146, 374: 15.4634146, 375: 15.4634146, 380: 15.4634146, 414: 15.4634146, 735: 17.6764706, 737: 17.6764706, 739: 17.6764706, 764: 17.6764706, 767: 17.6764706, 702: 17.6764706, 704: 17.6764706, 705: 17.6764706, 706: 17.6764706, 707: 17.6764706, 733: 17.6764706, 734: 17.6764706, 797: 17.6764706, 798: 17.6764706, 799: 17.6764706, 801: 17.6764706, 802: 17.6764706, 803: 17.6764706, 804: 17.6764706, 834: 17.6764706, 835: 17.6764706, 743: 17.6764706, 771: 17.6764706, 774: 17.6764706, 775: 17.6764706, 738: 17.6764706, 740: 17.6764706, 768: 17.6764706, 769: 17.6764706, 770: 17.6764706, 741: 619.7058824, 742: 619.7058824, 772: 619.7058824, 773: 619.7058824, 162: 140.5588235, 165: 140.5588235, 158: 140.5588235, 213: 140.5588235, 215: 140.5588235, 160: 140.5588235, 123: 140.5588235, 214: 140.5588235, 256: 140.5588235, 255: 140.5588235, 127: 140.5588235, 163: 140.5588235, 171: 140.5588235, 216: 140.5588235, 217: 140.5588235, 219: 140.5588235, 166: 140.5588235, 172: 140.5588235, 131: 74.9428571, 167: 74.9428571, 1262: 74.9428571, 170: 140.5588235, 205: 140.5588235, 208: 140.5588235, 209: 140.5588235, 168: 140.5588235, 164: 140.5588235, 169: 140.5588235, 212: 140.5588235, 159: 140.5588235, 126: 140.5588235, 129: 140.5588235, 130: 140.5588235, 132: 140.5588235, 1475: 12.3333333, 1476: 12.3333333, 1478: 12.3333333, 1368: 12.3333333, 1369: 12.3333333, 1470: 12.3333333, 1467: 12.3333333, 1468: 12.3333333, 1469: 12.3333333, 1567: 12.3333333, 1646: 12.3333333, 1556: 12.3333333, 1557: 12.3333333, 1559: 12.3333333, 1560: 12.3333333, 1472: 12.3333333, 1473: 12.3333333, 1558: 12.3333333, 1561: 12.3333333, 1562: 12.3333333, 1564: 12.3333333, 1360: 12.3333333, 1363: 12.3333333, 1364: 12.3333333, 1365: 12.3333333, 1366: 12.3333333, 1463: 12.3333333, 1466: 12.3333333, 1474: 12.3333333, 1477: 12.3333333, 1563: 12.3333333, 1568: 12.3333333, 1643: 12.3333333, 1644: 12.3333333, 1645: 12.3333333, 1328: 8.8407767, 1329: 8.8407767, 1330: 8.8407767, 1331: 8.8407767, 1332: 8.8407767, 1333: 8.8407767, 1435: 8.8407767, 1437: 8.8407767, 1438: 8.8407767, 1439: 8.8407767, 1440: 8.8407767, 1441: 8.8407767, 1442: 8.8407767, 1443: 8.8407767, 1444: 8.8407767, 1481: 8.8407767, 1539: 8.8407767, 1540: 8.8407767, 1541: 8.8407767, 1542: 8.8407767, 1543: 8.8407767, 1544: 8.8407767, 1565: 8.8407767, 1566: 8.8407767, 1630: 8.8407767, 1631: 8.8407767, 1632: 8.8407767, 1633: 8.8407767, 1636: 8.8407767, 1695: 8.8407767, 1696: 8.8407767, 1699: 8.8407767, 1225: 12.3333333, 1226: 12.3333333, 1229: 12.3333333, 1230: 12.3333333, 1281: 12.3333333, 1282: 12.3333333, 1283: 12.3333333, 1284: 12.3333333, 1285: 12.3333333, 1286: 12.3333333, 1287: 12.3333333, 1288: 12.3333333, 1289: 12.3333333, 1367: 12.3333333, 1370: 12.3333333, 1373: 12.3333333, 1471: 12.3333333, 790: 22.75, 791: 22.75, 793: 22.75, 878: 22.75, 880: 22.75, 881: 22.75, 913: 22.75, 914: 22.75, 915: 22.75, 916: 22.75, 917: 22.75, 920: 22.75, 867: 22.75, 829: 22.75, 903: 22.75, 907: 22.75, 908: 22.75, 912: 22.75, 828: 22.75, 868: 22.75, 901: 22.75, 871: 22.75, 872: 22.75, 873: 22.75, 870: 22.75, 826: 22.75, 827: 22.75, 836: 22.75, 841: 22.75, 879: 22.75, 882: 22.75, 883: 22.75, 884: 22.75, 885: 22.75, 918: 22.75, 794: 22.75, 795: 22.75, 796: 22.75, 800: 22.75, 830: 22.75, 831: 22.75, 832: 22.75, 833: 22.75, 837: 22.75, 874: 22.75, 875: 22.75, 876: 22.75, 877: 22.75, 909: 22.75, 910: 22.75, 911: 22.75, 902: 22.75, 904: 22.75, 905: 22.75, 906: 22.75, 792: 22.75, 1208: 58.2, 1211: 58.2, 1162: 3831.0, 1079: 58.2, 1122: 58.2, 1123: 58.2, 1124: 58.2, 1125: 58.2, 1126: 58.2, 1129: 58.2, 1163: 58.2, 1164: 58.2, 1165: 58.2, 1167: 58.2, 1169: 58.2, 1170: 58.2, 1116: 58.2, 1121: 58.2, 1120: 58.2, 1075: 58.2, 1080: 58.2, 1119: 58.2, 1071: 58.2, 1072: 58.2, 1076: 58.2, 1115: 58.2, 1118: 58.2, 1160: 58.2, 1161: 58.2, 1166: 58.2, 462: 50.0384615, 388: 50.0384615, 389: 50.0384615, 390: 50.0384615, 391: 50.0384615, 464: 50.0384615, 431: 50.0384615, 432: 50.0384615, 463: 3831.0, 465: 3831.0, 468: 3831.0, 435: 50.0384615, 436: 50.0384615, 439: 50.0384615, 440: 50.0384615, 466: 50.0384615, 469: 50.0384615, 470: 50.0384615, 331: 50.0384615, 336: 50.0384615, 353: 50.0384615, 427: 50.0384615, 428: 50.0384615, 429: 50.0384615, 393: 50.0384615, 394: 50.0384615, 430: 50.0384615, 335: 50.0384615, 356: 50.0384615, 357: 50.0384615, 358: 50.0384615, 359: 50.0384615, 363: 50.0384615, 392: 50.0384615, 395: 50.0384615, 396: 50.0384615, 397: 50.0384615, 398: 50.0384615, 352: 50.0384615, 354: 50.0384615, 355: 50.0384615, 385: 50.0384615, 1619: 8.8407767, 1620: 8.8407767, 1621: 8.8407767, 1624: 8.8407767, 1628: 8.8407767, 1693: 8.8407767, 1694: 8.8407767, 1545: 8.8407767, 1546: 8.8407767, 1547: 8.8407767, 1548: 8.8407767, 1549: 8.8407767, 1550: 8.8407767, 1551: 8.8407767, 1634: 8.8407767, 1635: 8.8407767, 1637: 8.8407767, 1638: 8.8407767, 1639: 8.8407767, 1640: 8.8407767, 1641: 8.8407767, 1642: 8.8407767, 1700: 8.8407767, 1701: 8.8407767, 1703: 8.8407767, 1704: 8.8407767, 1705: 8.8407767, 1706: 8.8407767, 1902: 8.8407767, 1905: 8.8407767, 1906: 8.8407767, 1907: 8.8407767, 1946: 8.8407767, 1947: 8.8407767, 1948: 8.8407767, 1950: 8.8407767, 1951: 8.8407767, 1952: 8.8407767, 1953: 8.8407767, 1990: 8.8407767, 1991: 8.8407767, 1993: 8.8407767, 1994: 8.8407767, 1996: 8.8407767, 1627: 8.8407767, 1629: 8.8407767, 1928: 8.8407767, 1929: 8.8407767, 1932: 8.8407767, 1933: 8.8407767, 1937: 8.8407767, 1969: 8.8407767, 1970: 8.8407767, 1971: 8.8407767, 1972: 8.8407767, 1973: 8.8407767, 1974: 8.8407767, 1975: 8.8407767, 1976: 8.8407767, 1977: 8.8407767, 1978: 8.8407767, 1979: 8.8407767, 1980: 8.8407767, 1981: 8.8407767, 1983: 8.8407767, 1984: 8.8407767, 1988: 8.8407767, 2008: 8.8407767, 2009: 8.8407767, 2010: 8.8407767, 2011: 8.8407767, 2012: 8.8407767, 2013: 8.8407767, 2014: 8.8407767, 2015: 8.8407767, 2016: 8.8407767, 2017: 8.8407767, 2018: 8.8407767, 2019: 8.8407767, 2020: 8.8407767, 2021: 8.8407767, 2022: 8.8407767, 2023: 8.8407767, 2024: 8.8407767, 2025: 8.8407767, 2026: 8.8407767, 2027: 8.8407767, 2028: 8.8407767, 2029: 8.8407767, 2030: 8.8407767, 2033: 8.8407767, 2046: 8.8407767, 2047: 8.8407767, 2048: 8.8407767, 2049: 8.8407767, 2050: 8.8407767, 2051: 8.8407767, 2052: 8.8407767, 2053: 8.8407767, 2054: 8.8407767, 2055: 8.8407767, 2056: 8.8407767, 2058: 8.8407767, 2071: 8.8407767, 2072: 8.8407767, 2074: 8.8407767, 2075: 8.8407767, 1842: 8.8407767, 1843: 8.8407767, 1844: 8.8407767, 1845: 8.8407767, 1847: 8.8407767, 1848: 8.8407767, 1885: 8.8407767, 1886: 8.8407767, 1887: 8.8407767, 1888: 8.8407767, 1889: 8.8407767, 1890: 8.8407767, 1891: 8.8407767, 1892: 8.8407767, 1893: 8.8407767, 1927: 8.8407767, 1930: 8.8407767, 1931: 8.8407767, 1934: 8.8407767, 1799: 8.8407767, 1804: 8.8407767, 2108: 8.8407767, 2109: 8.8407767, 2110: 8.8407767, 2111: 8.8407767, 2112: 8.8407767, 2121: 8.8407767, 2122: 8.8407767, 2123: 8.8407767, 2124: 8.8407767, 2125: 8.8407767, 2126: 8.8407767, 2127: 8.8407767, 2128: 8.8407767, 2136: 8.8407767, 2137: 8.8407767, 2138: 8.8407767, 2139: 8.8407767, 2140: 8.8407767, 2141: 8.8407767, 2142: 8.8407767, 2143: 8.8407767, 2151: 8.8407767, 2154: 8.8407767, 2155: 8.8407767, 2156: 8.8407767, 2158: 8.8407767, 2159: 8.8407767, 2160: 8.8407767, 2161: 8.8407767, 2168: 8.8407767, 2170: 8.8407767, 1765: 8.8407767, 1766: 8.8407767, 1768: 8.8407767, 1769: 8.8407767, 1770: 8.8407767, 1806: 8.8407767, 1809: 8.8407767, 1810: 8.8407767, 1811: 8.8407767, 1812: 8.8407767, 1813: 8.8407767, 1814: 8.8407767, 1815: 8.8407767, 1816: 8.8407767, 1817: 8.8407767, 1818: 8.8407767, 1819: 8.8407767, 1821: 8.8407767, 1858: 8.8407767, 1861: 8.8407767, 1862: 8.8407767, 1865: 8.8407767, 1752: 8.8407767, 1839: 8.8407767, 1884: 8.8407767, 1707: 8.8407767, 1708: 8.8407767, 1709: 8.8407767, 1710: 8.8407767, 1820: 8.8407767, 1822: 8.8407767, 1823: 8.8407767, 1824: 8.8407767, 1825: 8.8407767, 1826: 8.8407767, 1827: 8.8407767, 1828: 8.8407767, 1829: 8.8407767, 1830: 8.8407767, 1831: 8.8407767, 1870: 8.8407767, 1873: 8.8407767, 1874: 8.8407767, 1875: 8.8407767, 1876: 8.8407767, 1877: 8.8407767, 1878: 8.8407767, 1879: 8.8407767, 1880: 8.8407767, 1881: 8.8407767, 1882: 8.8407767, 1883: 8.8407767, 1921: 8.8407767, 1924: 8.8407767, 1925: 8.8407767, 1926: 8.8407767, 1802: 8.8407767, 1803: 8.8407767, 1897: 8.8407767, 1900: 8.8407767, 1903: 8.8407767, 1759: 8.8407767, 1760: 8.8407767, 1798: 8.8407767, 1801: 8.8407767, 1856: 8.8407767, 1995: 8.8407767, 1999: 8.8407767, 2000: 8.8407767, 2003: 8.8407767, 2004: 8.8407767, 2007: 8.8407767, 2031: 8.8407767, 2032: 8.8407767, 2034: 8.8407767, 2035: 8.8407767, 2036: 8.8407767, 2037: 8.8407767, 2038: 8.8407767, 2039: 8.8407767, 2040: 8.8407767, 2041: 8.8407767, 2042: 8.8407767, 2043: 8.8407767, 2044: 8.8407767, 2045: 8.8407767, 2064: 8.8407767, 2067: 8.8407767, 2068: 8.8407767, 2069: 8.8407767, 2070: 8.8407767, 2091: 8.8407767, 1846: 8.8407767, 1849: 8.8407767, 1852: 8.8407767, 2145: 8.8407767, 2148: 8.8407767, 2149: 8.8407767, 2150: 8.8407767, 2152: 8.8407767, 2153: 8.8407767, 2157: 8.8407767, 2162: 8.8407767, 2163: 8.8407767, 2164: 8.8407767, 2165: 8.8407767, 2166: 8.8407767, 2167: 8.8407767, 2169: 8.8407767, 2171: 8.8407767, 2172: 8.8407767, 2173: 8.8407767, 2174: 8.8407767, 2175: 8.8407767, 2176: 8.8407767, 2177: 8.8407767, 2178: 8.8407767, 2179: 8.8407767, 2180: 8.8407767, 2181: 8.8407767, 2182: 8.8407767, 2183: 8.8407767, 2184: 8.8407767, 2185: 8.8407767, 2186: 8.8407767, 2187: 8.8407767, 1793: 8.8407767, 1795: 8.8407767, 1796: 8.8407767, 1840: 8.8407767, 1841: 8.8407767, 1807: 8.8407767, 1853: 8.8407767, 1854: 8.8407767, 1805: 8.8407767, 1808: 8.8407767, 1850: 8.8407767, 1851: 8.8407767, 1855: 8.8407767, 1857: 8.8407767, 1859: 8.8407767, 1860: 8.8407767, 1864: 8.8407767, 1901: 8.8407767, 1904: 8.8407767, 1894: 8.8407767, 1895: 8.8407767, 1896: 8.8407767, 1898: 8.8407767, 1899: 8.8407767, 1935: 8.8407767, 1936: 8.8407767, 1938: 8.8407767, 1939: 8.8407767, 1940: 8.8407767, 1941: 8.8407767, 1942: 8.8407767, 1943: 8.8407767, 1944: 8.8407767, 1945: 8.8407767, 1949: 8.8407767, 1982: 8.8407767, 1985: 8.8407767, 1986: 8.8407767, 1987: 8.8407767, 1989: 8.8407767, 1992: 8.8407767, 1697: 8.8407767, 1698: 8.8407767, 1702: 8.8407767, 1751: 8.8407767, 1753: 8.8407767, 1755: 8.8407767, 1756: 8.8407767, 1794: 8.8407767, 1797: 8.8407767, 1800: 8.8407767, 1754: 8.8407767, 1757: 8.8407767, 1758: 8.8407767, 1761: 8.8407767, 1762: 8.8407767, 1763: 8.8407767, 1764: 8.8407767, 1767: 8.8407767, 4: 8.8407767, 2073: 8.8407767, 2076: 8.8407767, 2077: 8.8407767, 2094: 8.8407767, 2095: 8.8407767, 2096: 8.8407767, 2097: 8.8407767, 2098: 8.8407767, 2101: 8.8407767, 2113: 8.8407767, 2114: 8.8407767, 2115: 8.8407767, 2116: 8.8407767, 2117: 8.8407767, 2118: 8.8407767, 2119: 8.8407767, 2120: 8.8407767, 2129: 8.8407767, 2130: 8.8407767, 2131: 8.8407767, 2132: 8.8407767, 2133: 8.8407767, 2134: 8.8407767, 2135: 8.8407767, 2144: 8.8407767, 2146: 8.8407767, 2147: 8.8407767, 1019: 18.0689655, 1021: 18.0689655, 1026: 18.0689655, 1066: 18.0689655, 1191: 18.0689655, 1321: 18.0689655, 1322: 18.0689655, 1323: 18.0689655, 1324: 18.0689655, 1325: 18.0689655, 1326: 18.0689655, 1327: 18.0689655, 1423: 18.0689655, 1424: 18.0689655, 1425: 18.0689655, 1426: 18.0689655, 1427: 18.0689655, 1428: 18.0689655, 1429: 18.0689655, 1430: 18.0689655, 1431: 18.0689655, 1432: 18.0689655, 1433: 18.0689655, 1434: 18.0689655, 1436: 18.0689655, 1530: 18.0689655, 1531: 18.0689655, 1532: 18.0689655, 1533: 18.0689655, 1534: 18.0689655, 1535: 18.0689655, 1536: 18.0689655, 1537: 18.0689655, 1538: 18.0689655, 1623: 18.0689655, 1625: 18.0689655, 1626: 18.0689655, 2057: 8.8407767, 2059: 8.8407767, 2060: 8.8407767, 2061: 8.8407767, 2062: 8.8407767, 2063: 8.8407767, 2065: 8.8407767, 2066: 8.8407767, 2078: 8.8407767, 2079: 8.8407767, 2080: 8.8407767, 2081: 8.8407767, 2082: 8.8407767, 2083: 8.8407767, 2084: 8.8407767, 2085: 8.8407767, 2086: 8.8407767, 2087: 8.8407767, 2088: 8.8407767, 2089: 8.8407767, 2090: 8.8407767, 2092: 8.8407767, 2093: 8.8407767, 2099: 8.8407767, 2100: 8.8407767, 2102: 8.8407767, 2103: 8.8407767, 2104: 8.8407767, 2105: 8.8407767, 2106: 8.8407767, 2107: 8.8407767, 1863: 8.8407767, 1866: 8.8407767, 1867: 8.8407767, 1868: 8.8407767, 1869: 8.8407767, 1871: 8.8407767, 1872: 8.8407767, 1908: 8.8407767, 1909: 8.8407767, 1910: 8.8407767, 1911: 8.8407767, 1912: 8.8407767, 1913: 8.8407767, 1914: 8.8407767, 1915: 8.8407767, 1916: 8.8407767, 1917: 8.8407767, 1918: 8.8407767, 1919: 8.8407767, 1920: 8.8407767, 1922: 8.8407767, 1923: 8.8407767, 1954: 8.8407767, 1955: 8.8407767, 1956: 8.8407767, 1957: 8.8407767, 1958: 8.8407767, 1959: 8.8407767, 1960: 8.8407767, 1961: 8.8407767, 1962: 8.8407767, 1963: 8.8407767, 1964: 8.8407767, 1965: 8.8407767, 1966: 8.8407767, 1967: 8.8407767, 1968: 8.8407767, 1997: 8.8407767, 1998: 8.8407767, 2001: 8.8407767, 2002: 8.8407767, 2005: 8.8407767, 2006: 8.8407767, 602: 122.6111111, 605: 122.6111111, 663: 122.6111111, 628: 122.6111111, 660: 122.6111111, 662: 122.6111111, 585: 122.6111111, 595: 122.6111111, 614: 122.6111111, 615: 122.6111111, 616: 122.6111111, 617: 122.6111111, 618: 122.6111111, 639: 122.6111111, 603: 122.6111111, 604: 122.6111111, 661: 122.6111111, 629: 122.6111111, 630: 122.6111111, 667: 122.6111111, 634: 122.6111111, 664: 122.6111111, 607: 122.6111111, 608: 122.6111111, 633: 122.6111111, 665: 122.6111111, 591: 122.6111111, 593: 122.6111111, 594: 122.6111111, 596: 122.6111111, 609: 122.6111111, 610: 122.6111111, 613: 122.6111111, 635: 122.6111111, 638: 122.6111111, 597: 122.6111111, 598: 122.6111111, 599: 122.6111111, 611: 122.6111111, 612: 122.6111111, 636: 122.6111111, 600: 122.6111111, 625: 122.6111111, 626: 122.6111111, 586: 122.6111111, 587: 122.6111111, 588: 122.6111111, 589: 122.6111111, 590: 122.6111111, 592: 122.6111111, 606: 122.6111111, 632: 122.6111111, 601: 122.6111111, 631: 122.6111111, 1349: 74.9428571, 1344: 74.9428571, 1263: 74.9428571, 1460: 74.9428571, 1461: 74.9428571, 1465: 74.9428571, 1464: 74.9428571, 1554: 74.9428571, 1555: 74.9428571, 1343: 74.9428571, 1347: 74.9428571, 1456: 74.9428571, 1457: 74.9428571, 1448: 74.9428571, 1458: 74.9428571, 1459: 74.9428571, 1462: 74.9428571, 1264: 74.9428571, 1447: 74.9428571, 1450: 74.9428571, 1268: 74.9428571, 1348: 74.9428571, 1553: 74.9428571, 1453: 74.9428571, 1350: 74.9428571, 1452: 74.9428571, 1352: 74.9428571, 1353: 74.9428571, 1455: 74.9428571, 1346: 74.9428571, 1451: 74.9428571, 1454: 74.9428571, 812: 31.2424242, 839: 31.2424242, 848: 31.2424242, 853: 31.2424242, 805: 31.2424242, 806: 31.2424242, 893: 31.2424242, 894: 31.2424242, 813: 31.2424242, 816: 31.2424242, 846: 31.2424242, 847: 31.2424242, 850: 31.2424242, 811: 31.2424242, 814: 31.2424242, 843: 31.2424242, 809: 31.2424242, 810: 31.2424242, 807: 31.2424242, 808: 31.2424242, 838: 31.2424242, 776: 31.2424242, 777: 31.2424242, 778: 31.2424242, 815: 31.2424242, 817: 31.2424242, 851: 31.2424242, 852: 31.2424242, 854: 31.2424242, 855: 31.2424242, 856: 31.2424242, 857: 31.2424242, 892: 31.2424242, 1776: 9.1184211, 1777: 9.1184211, 1832: 9.1184211, 1833: 9.1184211, 1773: 9.1184211, 1721: 9.1184211, 1771: 9.1184211, 1772: 9.1184211, 1592: 9.1184211, 1659: 9.1184211, 1662: 9.1184211, 1723: 9.1184211, 1780: 9.1184211, 1781: 9.1184211, 1782: 9.1184211, 1785: 9.1184211, 1834: 9.1184211, 1835: 9.1184211, 1836: 9.1184211, 1837: 9.1184211, 1599: 9.1184211, 1668: 9.1184211, 1669: 9.1184211, 1671: 9.1184211, 1674: 9.1184211, 1732: 9.1184211, 1733: 9.1184211, 1588: 9.1184211, 1653: 9.1184211, 1655: 9.1184211, 1658: 9.1184211, 1719: 9.1184211, 1725: 9.1184211, 1726: 9.1184211, 1729: 9.1184211, 1730: 9.1184211, 1774: 9.1184211, 1775: 9.1184211, 1778: 9.1184211, 1779: 9.1184211, 1591: 9.1184211, 1660: 9.1184211, 1661: 9.1184211, 1663: 9.1184211, 1666: 9.1184211, 1724: 9.1184211, 1727: 9.1184211, 1673: 9.1184211, 1678: 9.1184211, 1735: 9.1184211, 1736: 9.1184211, 1737: 9.1184211, 1738: 9.1184211, 1739: 9.1184211, 1741: 9.1184211, 1742: 9.1184211, 1587: 9.1184211, 1656: 9.1184211, 1657: 9.1184211, 1720: 9.1184211, 1783: 9.1184211, 1784: 9.1184211, 1786: 9.1184211, 1787: 9.1184211, 1788: 9.1184211, 1789: 9.1184211, 1790: 9.1184211, 1792: 9.1184211, 1838: 9.1184211, 1664: 9.1184211, 1665: 9.1184211, 1667: 9.1184211, 1670: 9.1184211, 1728: 9.1184211, 1731: 9.1184211, 1734: 9.1184211, 524: 49.7692308, 522: 49.7692308, 527: 49.7692308, 521: 49.7692308, 555: 49.7692308, 556: 49.7692308, 558: 49.7692308, 561: 49.7692308, 582: 49.7692308, 583: 49.7692308, 492: 49.7692308, 491: 49.7692308, 520: 49.7692308, 178: 13.8823529, 179: 13.8823529, 180: 13.8823529, 183: 13.8823529, 68: 13.8823529, 84: 13.8823529, 107: 13.8823529, 108: 13.8823529, 110: 13.8823529, 111: 13.8823529, 109: 619.7058824, 142: 619.7058824, 143: 619.7058824, 134: 13.8823529, 177: 13.8823529, 101: 13.8823529, 103: 13.8823529, 5: 13.8823529, 6: 13.8823529, 7: 13.8823529, 8: 13.8823529, 173: 13.8823529, 174: 13.8823529, 175: 13.8823529, 176: 13.8823529, 137: 13.8823529, 181: 13.8823529, 104: 13.8823529, 105: 13.8823529, 139: 13.8823529, 102: 13.8823529, 136: 13.8823529, 138: 13.8823529, 182: 13.8823529, 187: 13.8823529, 67: 13.8823529, 69: 13.8823529, 106: 13.8823529, 184: 13.8823529, 185: 13.8823529, 186: 13.8823529, 225: 13.8823529, 33: 13.8823529, 34: 13.8823529, 35: 13.8823529, 36: 13.8823529, 40: 13.8823529, 41: 13.8823529, 42: 13.8823529, 43: 13.8823529, 47: 13.8823529, 48: 13.8823529, 49: 13.8823529, 50: 13.8823529, 51: 13.8823529, 52: 13.8823529, 53: 13.8823529, 54: 13.8823529, 63: 13.8823529, 64: 13.8823529, 65: 13.8823529, 66: 13.8823529, 133: 13.8823529, 135: 13.8823529, 144: 13.8823529, 145: 13.8823529, 140: 13.8823529, 141: 13.8823529, 1198: 2043.5454545, 1253: 2043.5454545, 1192: 2043.5454545, 1193: 2043.5454545, 1149: 2043.5454545, 1194: 2043.5454545, 2: 2043.5454545, 1147: 2043.5454545, 1150: 2043.5454545, 1195: 2043.5454545, 1104: 2043.5454545, 371: 21.1851852, 372: 21.1851852, 376: 21.1851852, 514: 21.1851852, 515: 21.1851852, 546: 21.1851852, 547: 21.1851852, 416: 21.1851852, 417: 21.1851852, 451: 21.1851852, 452: 21.1851852, 453: 21.1851852, 454: 21.1851852, 457: 21.1851852, 483: 21.1851852, 544: 21.1851852, 545: 21.1851852, 549: 21.1851852, 484: 21.1851852, 486: 21.1851852, 410: 21.1851852, 411: 21.1851852, 412: 21.1851852, 413: 21.1851852, 485: 21.1851852, 513: 21.1851852, 148: 26.6590909, 153: 26.6590909, 196: 26.6590909, 149: 26.6590909, 192: 26.6590909, 193: 26.6590909, 194: 26.6590909, 195: 26.6590909, 236: 26.6590909, 124: 26.6590909, 155: 26.6590909, 114: 26.6590909, 146: 26.6590909, 156: 26.6590909, 161: 26.6590909, 202: 26.6590909, 204: 26.6590909, 207: 26.6590909, 152: 26.6590909, 157: 26.6590909, 118: 26.6590909, 147: 26.6590909, 150: 26.6590909, 151: 26.6590909, 197: 26.6590909, 198: 26.6590909, 199: 26.6590909, 239: 26.6590909, 240: 26.6590909, 241: 26.6590909, 243: 26.6590909, 244: 26.6590909, 245: 26.6590909, 246: 26.6590909, 247: 26.6590909, 250: 26.6590909, 200: 26.6590909, 201: 26.6590909, 203: 26.6590909, 83: 26.6590909, 86: 26.6590909, 112: 26.6590909, 113: 26.6590909, 115: 26.6590909, 637: 210.5833333, 670: 210.5833333, 674: 210.5833333, 675: 210.5833333, 701: 210.5833333, 668: 210.5833333, 669: 210.5833333, 725: 210.5833333, 642: 210.5833333, 672: 210.5833333, 673: 210.5833333, 696: 210.5833333, 697: 210.5833333, 703: 210.5833333, 698: 210.5833333, 699: 210.5833333, 640: 210.5833333, 641: 210.5833333, 643: 210.5833333, 644: 210.5833333, 666: 210.5833333, 671: 210.5833333, 700: 210.5833333, 722: 210.5833333, 749: 31.6896552, 750: 31.6896552, 779: 31.6896552, 780: 31.6896552, 785: 31.6896552, 788: 31.6896552, 724: 31.6896552, 748: 31.6896552, 751: 31.6896552, 715: 31.6896552, 716: 31.6896552, 744: 31.6896552, 745: 31.6896552, 746: 31.6896552, 753: 31.6896552, 758: 31.6896552, 784: 31.6896552, 786: 31.6896552, 787: 31.6896552, 789: 31.6896552, 723: 31.6896552, 752: 31.6896552, 781: 31.6896552, 782: 31.6896552, 710: 31.6896552, 711: 31.6896552, 712: 31.6896552, 754: 31.6896552, 783: 31.6896552, 1711: 67.8235294, 1713: 67.8235294, 1714: 67.8235294, 1480: 67.8235294, 1485: 67.8235294, 1569: 67.8235294, 1570: 67.8235294, 1573: 67.8235294, 1576: 67.8235294, 1571: 67.8235294, 1572: 67.8235294, 1649: 67.8235294, 1654: 67.8235294, 1712: 67.8235294, 1715: 67.8235294, 1716: 67.8235294, 1582: 67.8235294, 1583: 67.8235294, 1651: 67.8235294, 1652: 67.8235294, 1650: 67.8235294, 1717: 67.8235294, 1718: 67.8235294, 1722: 67.8235294, 1579: 67.8235294, 1581: 67.8235294, 1584: 67.8235294, 1648: 67.8235294, 1574: 67.8235294, 1575: 67.8235294, 1577: 67.8235294, 1578: 67.8235294, 1580: 67.8235294, 1647: 67.8235294, 227: 24.4827586, 228: 24.4827586, 229: 24.4827586, 230: 24.4827586, 274: 24.4827586, 275: 24.4827586, 302: 24.4827586, 266: 24.4827586, 267: 24.4827586, 190: 24.4827586, 191: 24.4827586, 231: 24.4827586, 232: 24.4827586, 235: 24.4827586, 242: 24.4827586, 272: 24.4827586, 273: 24.4827586, 276: 24.4827586, 226: 24.4827586, 233: 24.4827586, 234: 24.4827586, 237: 24.4827586, 238: 24.4827586, 268: 24.4827586, 269: 24.4827586, 270: 24.4827586, 271: 24.4827586, 188: 24.4827586, 189: 24.4827586, 985: 28.5915493, 987: 28.5915493, 988: 28.5915493, 1031: 28.5915493, 1032: 28.5915493, 1034: 28.5915493, 1029: 28.5915493, 1030: 28.5915493, 1074: 28.5915493, 1077: 28.5915493, 944: 28.5915493, 947: 28.5915493, 978: 28.5915493, 979: 28.5915493, 981: 28.5915493, 984: 28.5915493, 919: 28.5915493, 953: 28.5915493, 954: 28.5915493, 956: 28.5915493, 957: 28.5915493, 958: 28.5915493, 959: 28.5915493, 993: 28.5915493, 1035: 28.5915493, 1037: 28.5915493, 1038: 28.5915493, 1081: 28.5915493, 1082: 28.5915493, 937: 28.5915493, 938: 28.5915493, 939: 28.5915493, 940: 28.5915493, 941: 28.5915493, 942: 28.5915493, 943: 28.5915493, 973: 28.5915493, 974: 28.5915493, 975: 28.5915493, 977: 28.5915493, 980: 28.5915493, 983: 28.5915493, 1020: 28.5915493, 1023: 28.5915493, 1024: 28.5915493, 948: 28.5915493, 949: 28.5915493, 950: 28.5915493, 951: 28.5915493, 986: 28.5915493, 995: 28.5915493, 1000: 28.5915493, 991: 28.5915493, 994: 28.5915493, 996: 28.5915493, 1027: 28.5915493, 1033: 3831.0, 1078: 3831.0, 1025: 28.5915493, 1069: 28.5915493, 1070: 28.5915493, 1073: 28.5915493, 952: 28.5915493, 955: 28.5915493, 989: 28.5915493, 990: 28.5915493, 992: 28.5915493, 1028: 28.5915493, 945: 28.5915493, 946: 28.5915493, 982: 28.5915493, 73: 44.8292683, 74: 44.8292683, 121: 44.8292683, 122: 44.8292683, 154: 44.8292683, 87: 44.8292683, 88: 44.8292683, 89: 44.8292683, 91: 44.8292683, 80: 44.8292683, 81: 44.8292683, 82: 44.8292683, 37: 44.8292683, 38: 44.8292683, 39: 44.8292683, 44: 44.8292683, 85: 44.8292683, 90: 44.8292683, 70: 44.8292683, 71: 44.8292683, 72: 44.8292683, 75: 44.8292683, 0: 44.8292683, 45: 44.8292683, 55: 44.8292683, 56: 44.8292683, 76: 44.8292683, 77: 44.8292683, 119: 44.8292683, 120: 44.8292683, 78: 44.8292683, 79: 44.8292683, 116: 44.8292683, 117: 44.8292683, 690: 90.9230769, 721: 90.9230769, 717: 90.9230769, 718: 90.9230769, 686: 90.9230769, 687: 90.9230769, 691: 90.9230769, 713: 90.9230769, 714: 90.9230769, 695: 90.9230769, 719: 90.9230769, 720: 90.9230769, 747: 90.9230769, 1091: 12.0693069, 1134: 12.0693069, 1041: 12.0693069, 1044: 12.0693069, 1086: 12.0693069, 1089: 12.0693069, 1090: 12.0693069, 1093: 12.0693069, 1184: 12.0693069, 1186: 12.0693069, 1228: 12.0693069, 1231: 12.0693069, 1092: 12.0693069, 1140: 12.0693069, 1141: 12.0693069, 1176: 12.0693069, 1135: 12.0693069, 1136: 12.0693069, 3: 12.0693069, 1188: 12.0693069, 1190: 12.0693069, 1235: 12.0693069, 1236: 12.0693069, 1237: 12.0693069, 1238: 12.0693069, 1239: 12.0693069, 1240: 12.0693069, 1242: 12.0693069, 1294: 12.0693069, 999: 12.0693069, 1036: 12.0693069, 1039: 12.0693069, 1042: 12.0693069, 1003: 12.0693069, 1004: 12.0693069, 1040: 12.0693069, 1043: 12.0693069, 1005: 12.0693069, 1006: 12.0693069, 1007: 12.0693069, 1045: 12.0693069, 1046: 12.0693069, 1047: 12.0693069, 1048: 12.0693069, 1049: 12.0693069, 1050: 12.0693069, 1051: 12.0693069, 1052: 12.0693069, 1144: 12.0693069, 1145: 12.0693069, 1181: 12.0693069, 1183: 12.0693069, 1131: 12.0693069, 1132: 12.0693069, 1137: 12.0693069, 1171: 12.0693069, 1172: 12.0693069, 1173: 12.0693069, 1174: 12.0693069, 1175: 12.0693069, 1178: 12.0693069, 1220: 12.0693069, 1084: 12.0693069, 1127: 12.0693069, 1128: 12.0693069, 1130: 12.0693069, 1133: 12.0693069, 1168: 12.0693069, 961: 12.0693069, 962: 12.0693069, 963: 12.0693069, 964: 12.0693069, 965: 12.0693069, 997: 12.0693069, 998: 12.0693069, 1001: 12.0693069, 1002: 12.0693069, 1083: 12.0693069, 1085: 12.0693069, 1087: 12.0693069, 1088: 12.0693069, 1185: 12.0693069, 1187: 12.0693069, 1189: 12.0693069, 1232: 12.0693069, 1233: 12.0693069, 1234: 12.0693069, 1177: 12.0693069, 1179: 12.0693069, 1180: 12.0693069, 1182: 12.0693069, 1223: 12.0693069, 1224: 12.0693069, 1227: 12.0693069, 1094: 12.0693069, 1095: 12.0693069, 1096: 12.0693069, 1138: 12.0693069, 1139: 12.0693069, 1142: 12.0693069, 1143: 12.0693069, 285: 22.0, 288: 22.0, 253: 22.0, 257: 22.0, 206: 22.0, 210: 22.0, 211: 22.0, 248: 22.0, 251: 22.0, 252: 22.0, 304: 22.0, 305: 22.0, 307: 22.0, 308: 22.0, 311: 22.0, 309: 22.0, 277: 22.0, 278: 22.0, 281: 22.0, 291: 22.0, 292: 22.0, 286: 22.0, 289: 22.0, 290: 22.0, 279: 22.0, 280: 22.0, 284: 22.0, 303: 22.0, 306: 22.0, 287: 22.0, 310: 22.0, 249: 22.0, 254: 22.0, 282: 22.0, 283: 22.0, 312: 22.0, 313: 22.0, 525: 33.5121951, 534: 33.5121951, 535: 33.5121951, 539: 33.5121951, 567: 33.5121951, 570: 33.5121951, 526: 33.5121951, 559: 33.5121951, 493: 33.5121951, 496: 33.5121951, 499: 33.5121951, 528: 33.5121951, 529: 33.5121951, 497: 33.5121951, 498: 33.5121951, 503: 33.5121951, 467: 33.5121951, 471: 33.5121951, 472: 33.5121951, 500: 33.5121951, 501: 33.5121951, 504: 33.5121951, 564: 33.5121951, 565: 33.5121951, 560: 33.5121951, 562: 33.5121951, 530: 33.5121951, 531: 33.5121951, 563: 33.5121951, 502: 33.5121951, 507: 33.5121951, 532: 33.5121951, 533: 33.5121951, 536: 33.5121951, 566: 33.5121951, 568: 33.5121951, 569: 33.5121951, 572: 33.5121951, 573: 33.5121951, 494: 33.5121951, 495: 33.5121951, 13: 502.3333333, 10: 502.3333333, 11: 502.3333333, 12: 502.3333333, 18: 502.3333333, 19: 502.3333333, 20: 502.3333333, 21: 502.3333333, 22: 502.3333333, 23: 502.3333333, 24: 502.3333333, 25: 502.3333333, 26: 502.3333333, 27: 502.3333333, 28: 502.3333333, 29: 502.3333333, 30: 502.3333333, 31: 502.3333333, 32: 502.3333333, 14: 502.3333333, 9: 502.3333333, 15: 502.3333333, 16: 502.3333333, 17: 502.3333333, 657: 619.7058824, 659: 619.7058824, 688: 619.7058824, 693: 619.7058824, 658: 619.7058824, 692: 619.7058824, 656: 619.7058824, 694: 619.7058824, 689: 619.7058824, 627: 619.7058824, 92: 38.7272727, 95: 38.7272727, 98: 38.7272727, 125: 38.7272727, 96: 38.7272727, 97: 38.7272727, 99: 38.7272727, 100: 38.7272727, 128: 38.7272727, 94: 38.7272727, 93: 38.7272727, 1204: 390.7058824, 1112: 390.7058824, 1114: 390.7058824, 1117: 390.7058824, 1155: 390.7058824, 1153: 390.7058824, 1205: 390.7058824, 1158: 390.7058824, 1258: 390.7058824, 1203: 390.7058824, 1206: 390.7058824, 1201: 390.7058824, 1157: 390.7058824, 1261: 390.7058824, 1200: 390.7058824, 1156: 390.7058824, 1159: 390.7058824, 762: 63.1111111, 726: 63.1111111, 729: 63.1111111, 728: 63.1111111, 755: 63.1111111, 727: 63.1111111, 730: 63.1111111, 731: 63.1111111, 736: 63.1111111, 756: 63.1111111, 757: 63.1111111, 759: 63.1111111, 760: 63.1111111, 761: 63.1111111, 763: 63.1111111, 765: 63.1111111, 766: 63.1111111, 732: 63.1111111, 405: 11.8043478, 406: 11.8043478, 407: 11.8043478, 408: 11.8043478, 409: 11.8043478, 445: 11.8043478, 446: 11.8043478, 319: 11.8043478, 320: 11.8043478, 321: 11.8043478, 322: 11.8043478, 323: 11.8043478, 324: 11.8043478, 325: 11.8043478, 333: 11.8043478, 334: 11.8043478, 337: 11.8043478, 473: 11.8043478, 474: 11.8043478, 342: 11.8043478, 362: 11.8043478, 364: 11.8043478, 365: 11.8043478, 367: 11.8043478, 368: 11.8043478, 438: 11.8043478, 441: 11.8043478, 442: 11.8043478, 443: 11.8043478, 444: 11.8043478, 448: 11.8043478, 338: 11.8043478, 339: 11.8043478, 340: 11.8043478, 341: 11.8043478, 343: 11.8043478, 360: 11.8043478, 361: 11.8043478, 366: 11.8043478, 369: 11.8043478, 370: 11.8043478, 399: 11.8043478, 400: 11.8043478, 401: 11.8043478, 403: 11.8043478, 404: 11.8043478, 930: 88.0555556, 1056: 88.0555556, 1099: 88.0555556, 1100: 88.0555556, 1105: 88.0555556, 1013: 88.0555556, 1014: 88.0555556, 1057: 88.0555556, 1058: 88.0555556, 1059: 88.0555556, 1101: 88.0555556, 1146: 88.0555556, 972: 88.0555556, 931: 88.0555556, 1010: 88.0555556, 966: 88.0555556, 969: 88.0555556, 970: 88.0555556, 971: 88.0555556, 976: 88.0555556, 1008: 88.0555556, 1009: 88.0555556, 1011: 88.0555556, 1103: 88.0555556, 934: 88.0555556, 935: 88.0555556, 1055: 88.0555556, 1060: 88.0555556, 1053: 88.0555556, 1054: 88.0555556, 1097: 88.0555556, 1102: 88.0555556, 896: 88.0555556, 1098: 88.0555556, 968: 88.0555556, 967: 88.0555556, 1207: 45.8421053, 1209: 45.8421053, 1266: 45.8421053, 1214: 45.8421053, 1269: 45.8421053, 1265: 45.8421053, 1267: 45.8421053, 1272: 45.8421053, 1351: 45.8421053, 1354: 45.8421053, 1358: 45.8421053, 1274: 45.8421053, 1276: 45.8421053, 1221: 45.8421053, 1275: 45.8421053, 1277: 45.8421053, 1278: 45.8421053, 1279: 45.8421053, 1280: 45.8421053, 1359: 45.8421053, 1362: 45.8421053, 1210: 45.8421053, 1355: 45.8421053, 1356: 45.8421053, 1357: 45.8421053, 1361: 45.8421053, 1212: 45.8421053, 1213: 45.8421053, 1215: 45.8421053, 1216: 45.8421053, 1217: 45.8421053, 1218: 45.8421053, 1219: 45.8421053, 1222: 45.8421053, 1270: 45.8421053, 1273: 45.8421053, 1: 22.6956522, 584: 22.6956522, 580: 22.6956522, 578: 22.6956522, 579: 22.6956522, 581: 22.6956522, 548: 22.6956522, 550: 22.6956522, 551: 22.6956522, 552: 22.6956522, 553: 22.6956522, 554: 22.6956522, 557: 22.6956522, 1151: 3831.0, 1152: 3831.0, 1199: 3831.0, 1154: 3831.0, 1196: 3831.0, 1257: 3831.0, 1061: 18.0689655, 1062: 18.0689655, 1063: 18.0689655, 1202: 3831.0, 1197: 3831.0, 1254: 3831.0, 475: 9.25, 476: 9.25, 479: 9.25, 505: 9.25, 508: 9.25, 509: 9.25, 506: 9.25, 510: 9.25, 511: 9.25, 537: 9.25, 538: 9.25, 540: 9.25, 541: 9.25, 542: 9.25, 543: 9.25, 571: 9.25, 574: 9.25, 575: 9.25, 576: 9.25, 577: 9.25, 447: 9.25, 449: 9.25, 450: 9.25, 477: 9.25, 478: 9.25, 480: 9.25, 481: 9.25, 482: 9.25, 923: 29.0, 925: 29.0, 849: 29.0, 888: 29.0, 891: 29.0, 921: 29.0, 922: 29.0, 924: 29.0, 844: 29.0, 886: 29.0, 840: 29.0, 842: 29.0, 845: 29.0, 890: 29.0, 887: 29.0, 889: 29.0, 926: 29.0, 927: 29.0, 928: 29.0, 929: 29.0, 960: 29.0, 623: 21.1724138, 652: 21.1724138, 645: 21.1724138, 646: 21.1724138, 647: 21.1724138, 650: 21.1724138, 651: 21.1724138, 676: 21.1724138, 677: 21.1724138, 680: 21.1724138, 681: 21.1724138, 621: 21.1724138, 648: 21.1724138, 649: 21.1724138, 619: 21.1724138, 620: 21.1724138, 622: 21.1724138, 624: 21.1724138, 678: 21.1724138, 679: 21.1724138, 683: 21.1724138, 708: 21.1724138, 709: 21.1724138, 654: 21.1724138, 655: 21.1724138, 682: 21.1724138, 684: 21.1724138, 685: 21.1724138, 653: 21.1724138, 1292: 11.1538462, 1371: 11.1538462, 1372: 11.1538462, 1374: 11.1538462, 1377: 11.1538462, 1386: 11.1538462, 1387: 11.1538462, 1388: 11.1538462, 1389: 11.1538462, 1393: 11.1538462, 1490: 11.1538462, 1491: 11.1538462, 1492: 11.1538462, 1380: 11.1538462, 1382: 11.1538462, 1383: 11.1538462, 1385: 11.1538462, 1381: 11.1538462, 1479: 11.1538462, 1482: 11.1538462, 1290: 11.1538462, 1291: 11.1538462, 1293: 11.1538462, 1295: 11.1538462, 1296: 11.1538462, 1378: 11.1538462, 1379: 11.1538462, 1483: 11.1538462, 1484: 11.1538462, 1486: 11.1538462, 1489: 11.1538462, 1384: 11.1538462, 1487: 11.1538462, 1488: 11.1538462, 1493: 11.1538462, 1375: 11.1538462, 1376: 11.1538462, 1241: 11.1538462, 1243: 11.1538462, 1245: 11.1538462, 1297: 11.1538462, 1298: 11.1538462, 1299: 11.1538462, 1300: 11.1538462, 1301: 11.1538462, 1304: 11.1538462, 1244: 11.1538462, 1302: 11.1538462, 1303: 11.1538462, 1305: 11.1538462, 1308: 11.1538462, 1390: 11.1538462, 314: 40.6857143, 329: 40.6857143, 316: 40.6857143, 317: 40.6857143, 330: 40.6857143, 326: 40.6857143, 218: 40.6857143, 221: 40.6857143, 327: 40.6857143, 328: 40.6857143, 351: 40.6857143, 297: 40.6857143, 298: 40.6857143, 299: 40.6857143, 300: 40.6857143, 301: 40.6857143, 318: 40.6857143, 220: 40.6857143, 222: 40.6857143, 223: 40.6857143, 224: 40.6857143, 260: 40.6857143, 263: 40.6857143, 264: 40.6857143, 265: 40.6857143, 258: 40.6857143, 293: 40.6857143, 294: 40.6857143, 295: 40.6857143, 296: 40.6857143, 315: 40.6857143, 332: 40.6857143, 259: 40.6857143, 261: 40.6857143, 262: 40.6857143, 1064: 18.0689655, 1106: 18.0689655, 1107: 18.0689655, 1109: 18.0689655, 1110: 18.0689655, 1022: 18.0689655, 1012: 18.0689655, 1015: 18.0689655, 1016: 18.0689655, 1017: 18.0689655, 1018: 18.0689655, 1065: 18.0689655, 1108: 18.0689655, 1113: 18.0689655, 1148: 18.0689655, 1067: 18.0689655, 1068: 18.0689655, 1111: 18.0689655}

normalized_tile_pdf_dict ={895: 0.00099, 865: 0.00099, 823: 0.00099, 866: 0.00099, 821: 0.00099, 825: 0.00099, 897: 0.00099, 46: 0.00025, 57: 0.00025, 58: 0.00025, 59: 0.00025, 60: 0.00025, 61: 0.00025, 62: 0.00025, 864: 0.00099, 869: 0.00099, 862: 0.00099, 858: 0.00099, 859: 0.00099, 860: 0.00099, 818: 0.00099, 512: 0.00012, 824: 0.00099, 820: 0.00099, 861: 0.00099, 898: 0.00099, 899: 0.00099, 900: 0.00099, 932: 0.00099, 933: 0.00099, 936: 0.00099, 819: 0.00099, 402: 0.00012, 433: 0.00012, 434: 0.00012, 437: 0.00012, 516: 0.00012, 517: 0.00012, 518: 0.00012, 519: 0.00012, 523: 0.00012, 863: 0.00012, 822: 0.00099, 1512: 5e-05, 1513: 5e-05, 1517: 5e-05, 1605: 5e-05, 1601: 5e-05, 1602: 5e-05, 1603: 5e-05, 1604: 5e-05, 1607: 5e-05, 1608: 5e-05, 1672: 5e-05, 1675: 5e-05, 1400: 5e-05, 1499: 5e-05, 1502: 5e-05, 1503: 5e-05, 1505: 5e-05, 1506: 5e-05, 1313: 5e-05, 1314: 5e-05, 1317: 5e-05, 1399: 5e-05, 1402: 5e-05, 1403: 5e-05, 1404: 5e-05, 1405: 5e-05, 1408: 5e-05, 1409: 5e-05, 1413: 5e-05, 1507: 5e-05, 1510: 5e-05, 1511: 5e-05, 1514: 5e-05, 1312: 5e-05, 1315: 5e-05, 1310: 5e-05, 1394: 5e-05, 1395: 5e-05, 1396: 5e-05, 1397: 5e-05, 1398: 5e-05, 1401: 5e-05, 1392: 5e-05, 1494: 5e-05, 1495: 5e-05, 1496: 5e-05, 1497: 5e-05, 1498: 5e-05, 1585: 5e-05, 1586: 5e-05, 1504: 5e-05, 1508: 5e-05, 1509: 5e-05, 1593: 5e-05, 1594: 5e-05, 1595: 5e-05, 1596: 5e-05, 1597: 5e-05, 1598: 5e-05, 1600: 5e-05, 1500: 5e-05, 1501: 5e-05, 1589: 5e-05, 1590: 5e-05, 1306: 5e-05, 1307: 5e-05, 1309: 5e-05, 1311: 5e-05, 1391: 5e-05, 1316: 5e-05, 1318: 5e-05, 1320: 5e-05, 1406: 5e-05, 1407: 5e-05, 1410: 5e-05, 1411: 5e-05, 1520: 0.00013, 1609: 0.00013, 1612: 0.00013, 1744: 0.00013, 1745: 0.00013, 1746: 0.00013, 1791: 0.00013, 1618: 0.00013, 1622: 0.00013, 1685: 0.00013, 1687: 0.00013, 1688: 0.00013, 1689: 0.00013, 1690: 0.00013, 1691: 0.00013, 1692: 0.00013, 1747: 0.00013, 1748: 0.00013, 1749: 0.00013, 1750: 0.00013, 1676: 0.00013, 1677: 0.00013, 1679: 0.00013, 1680: 0.00013, 1681: 0.00013, 1682: 0.00013, 1686: 0.00013, 1740: 0.00013, 1743: 0.00013, 1319: 0.00013, 1414: 0.00013, 1415: 0.00013, 1416: 0.00013, 1418: 0.00013, 1419: 0.00013, 1420: 0.00013, 1421: 0.00013, 1422: 0.00013, 1519: 0.00013, 1522: 0.00013, 1523: 0.00013, 1526: 0.00013, 1527: 0.00013, 1524: 0.00013, 1525: 0.00013, 1528: 0.00013, 1529: 0.00013, 1610: 0.00013, 1611: 0.00013, 1613: 0.00013, 1614: 0.00013, 1615: 0.00013, 1616: 0.00013, 1617: 0.00013, 1683: 0.00013, 1684: 0.00013, 1516: 0.00013, 1521: 0.00013, 1606: 0.00013, 1412: 0.00013, 1417: 0.00013, 1515: 0.00013, 1518: 0.00013, 1260: 0.00176, 1246: 0.00176, 1248: 0.00176, 1336: 0.00176, 1341: 0.00176, 1446: 0.00176, 1271: 0.00025, 1345: 0.00025, 1337: 0.00176, 1338: 0.00176, 1259: 0.00176, 1342: 0.00176, 1251: 0.00176, 1249: 0.00176, 1250: 0.00176, 1252: 0.00176, 1255: 0.00176, 1340: 0.00176, 1256: 0.00176, 1335: 0.00176, 1334: 0.00176, 1552: 0.00176, 1449: 0.00176, 1247: 0.00176, 1339: 0.00176, 1445: 0.00176, 460: 8e-05, 461: 8e-05, 487: 8e-05, 488: 8e-05, 489: 8e-05, 490: 8e-05, 347: 8e-05, 377: 8e-05, 418: 8e-05, 419: 8e-05, 420: 8e-05, 421: 8e-05, 422: 8e-05, 425: 8e-05, 455: 8e-05, 456: 8e-05, 458: 8e-05, 459: 8e-05, 378: 8e-05, 379: 8e-05, 381: 8e-05, 415: 8e-05, 423: 8e-05, 424: 8e-05, 426: 8e-05, 346: 8e-05, 348: 8e-05, 349: 8e-05, 350: 8e-05, 382: 8e-05, 383: 8e-05, 384: 8e-05, 386: 8e-05, 387: 8e-05, 344: 8e-05, 345: 8e-05, 373: 8e-05, 374: 8e-05, 375: 8e-05, 380: 8e-05, 414: 8e-05, 735: 0.0001, 737: 0.0001, 739: 0.0001, 764: 0.0001, 767: 0.0001, 702: 0.0001, 704: 0.0001, 705: 0.0001, 706: 0.0001, 707: 0.0001, 733: 0.0001, 734: 0.0001, 797: 0.0001, 798: 0.0001, 799: 0.0001, 801: 0.0001, 802: 0.0001, 803: 0.0001, 804: 0.0001, 834: 0.0001, 835: 0.0001, 743: 0.0001, 771: 0.0001, 774: 0.0001, 775: 0.0001, 738: 0.0001, 740: 0.0001, 768: 0.0001, 769: 0.0001, 770: 0.0001, 741: 0.00339, 742: 0.00339, 772: 0.00339, 773: 0.00339, 162: 0.00077, 165: 0.00077, 158: 0.00077, 213: 0.00077, 215: 0.00077, 160: 0.00077, 123: 0.00077, 214: 0.00077, 256: 0.00077, 255: 0.00077, 127: 0.00077, 163: 0.00077, 171: 0.00077, 216: 0.00077, 217: 0.00077, 219: 0.00077, 166: 0.00077, 172: 0.00077, 131: 0.00041, 167: 0.00041, 1262: 0.00041, 170: 0.00077, 205: 0.00077, 208: 0.00077, 209: 0.00077, 168: 0.00077, 164: 0.00077, 169: 0.00077, 212: 0.00077, 159: 0.00077, 126: 0.00077, 129: 0.00077, 130: 0.00077, 132: 0.00077, 1475: 7e-05, 1476: 7e-05, 1478: 7e-05, 1368: 7e-05, 1369: 7e-05, 1470: 7e-05, 1467: 7e-05, 1468: 7e-05, 1469: 7e-05, 1567: 7e-05, 1646: 7e-05, 1556: 7e-05, 1557: 7e-05, 1559: 7e-05, 1560: 7e-05, 1472: 7e-05, 1473: 7e-05, 1558: 7e-05, 1561: 7e-05, 1562: 7e-05, 1564: 7e-05, 1360: 7e-05, 1363: 7e-05, 1364: 7e-05, 1365: 7e-05, 1366: 7e-05, 1463: 7e-05, 1466: 7e-05, 1474: 7e-05, 1477: 7e-05, 1563: 7e-05, 1568: 7e-05, 1643: 7e-05, 1644: 7e-05, 1645: 7e-05, 1328: 5e-05, 1329: 5e-05, 1330: 5e-05, 1331: 5e-05, 1332: 5e-05, 1333: 5e-05, 1435: 5e-05, 1437: 5e-05, 1438: 5e-05, 1439: 5e-05, 1440: 5e-05, 1441: 5e-05, 1442: 5e-05, 1443: 5e-05, 1444: 5e-05, 1481: 5e-05, 1539: 5e-05, 1540: 5e-05, 1541: 5e-05, 1542: 5e-05, 1543: 5e-05, 1544: 5e-05, 1565: 5e-05, 1566: 5e-05, 1630: 5e-05, 1631: 5e-05, 1632: 5e-05, 1633: 5e-05, 1636: 5e-05, 1695: 5e-05, 1696: 5e-05, 1699: 5e-05, 1225: 7e-05, 1226: 7e-05, 1229: 7e-05, 1230: 7e-05, 1281: 7e-05, 1282: 7e-05, 1283: 7e-05, 1284: 7e-05, 1285: 7e-05, 1286: 7e-05, 1287: 7e-05, 1288: 7e-05, 1289: 7e-05, 1367: 7e-05, 1370: 7e-05, 1373: 7e-05, 1471: 7e-05, 790: 0.00012, 791: 0.00012, 793: 0.00012, 878: 0.00012, 880: 0.00012, 881: 0.00012, 913: 0.00012, 914: 0.00012, 915: 0.00012, 916: 0.00012, 917: 0.00012, 920: 0.00012, 867: 0.00012, 829: 0.00012, 903: 0.00012, 907: 0.00012, 908: 0.00012, 912: 0.00012, 828: 0.00012, 868: 0.00012, 901: 0.00012, 871: 0.00012, 872: 0.00012, 873: 0.00012, 870: 0.00012, 826: 0.00012, 827: 0.00012, 836: 0.00012, 841: 0.00012, 879: 0.00012, 882: 0.00012, 883: 0.00012, 884: 0.00012, 885: 0.00012, 918: 0.00012, 794: 0.00012, 795: 0.00012, 796: 0.00012, 800: 0.00012, 830: 0.00012, 831: 0.00012, 832: 0.00012, 833: 0.00012, 837: 0.00012, 874: 0.00012, 875: 0.00012, 876: 0.00012, 877: 0.00012, 909: 0.00012, 910: 0.00012, 911: 0.00012, 902: 0.00012, 904: 0.00012, 905: 0.00012, 906: 0.00012, 792: 0.00012, 1208: 0.00032, 1211: 0.00032, 1162: 0.02098, 1079: 0.00032, 1122: 0.00032, 1123: 0.00032, 1124: 0.00032, 1125: 0.00032, 1126: 0.00032, 1129: 0.00032, 1163: 0.00032, 1164: 0.00032, 1165: 0.00032, 1167: 0.00032, 1169: 0.00032, 1170: 0.00032, 1116: 0.00032, 1121: 0.00032, 1120: 0.00032, 1075: 0.00032, 1080: 0.00032, 1119: 0.00032, 1071: 0.00032, 1072: 0.00032, 1076: 0.00032, 1115: 0.00032, 1118: 0.00032, 1160: 0.00032, 1161: 0.00032, 1166: 0.00032, 462: 0.00027, 388: 0.00027, 389: 0.00027, 390: 0.00027, 391: 0.00027, 464: 0.00027, 431: 0.00027, 432: 0.00027, 463: 0.02098, 465: 0.02098, 468: 0.02098, 435: 0.00027, 436: 0.00027, 439: 0.00027, 440: 0.00027, 466: 0.00027, 469: 0.00027, 470: 0.00027, 331: 0.00027, 336: 0.00027, 353: 0.00027, 427: 0.00027, 428: 0.00027, 429: 0.00027, 393: 0.00027, 394: 0.00027, 430: 0.00027, 335: 0.00027, 356: 0.00027, 357: 0.00027, 358: 0.00027, 359: 0.00027, 363: 0.00027, 392: 0.00027, 395: 0.00027, 396: 0.00027, 397: 0.00027, 398: 0.00027, 352: 0.00027, 354: 0.00027, 355: 0.00027, 385: 0.00027, 1619: 5e-05, 1620: 5e-05, 1621: 5e-05, 1624: 5e-05, 1628: 5e-05, 1693: 5e-05, 1694: 5e-05, 1545: 5e-05, 1546: 5e-05, 1547: 5e-05, 1548: 5e-05, 1549: 5e-05, 1550: 5e-05, 1551: 5e-05, 1634: 5e-05, 1635: 5e-05, 1637: 5e-05, 1638: 5e-05, 1639: 5e-05, 1640: 5e-05, 1641: 5e-05, 1642: 5e-05, 1700: 5e-05, 1701: 5e-05, 1703: 5e-05, 1704: 5e-05, 1705: 5e-05, 1706: 5e-05, 1902: 5e-05, 1905: 5e-05, 1906: 5e-05, 1907: 5e-05, 1946: 5e-05, 1947: 5e-05, 1948: 5e-05, 1950: 5e-05, 1951: 5e-05, 1952: 5e-05, 1953: 5e-05, 1990: 5e-05, 1991: 5e-05, 1993: 5e-05, 1994: 5e-05, 1996: 5e-05, 1627: 5e-05, 1629: 5e-05, 1928: 5e-05, 1929: 5e-05, 1932: 5e-05, 1933: 5e-05, 1937: 5e-05, 1969: 5e-05, 1970: 5e-05, 1971: 5e-05, 1972: 5e-05, 1973: 5e-05, 1974: 5e-05, 1975: 5e-05, 1976: 5e-05, 1977: 5e-05, 1978: 5e-05, 1979: 5e-05, 1980: 5e-05, 1981: 5e-05, 1983: 5e-05, 1984: 5e-05, 1988: 5e-05, 2008: 5e-05, 2009: 5e-05, 2010: 5e-05, 2011: 5e-05, 2012: 5e-05, 2013: 5e-05, 2014: 5e-05, 2015: 5e-05, 2016: 5e-05, 2017: 5e-05, 2018: 5e-05, 2019: 5e-05, 2020: 5e-05, 2021: 5e-05, 2022: 5e-05, 2023: 5e-05, 2024: 5e-05, 2025: 5e-05, 2026: 5e-05, 2027: 5e-05, 2028: 5e-05, 2029: 5e-05, 2030: 5e-05, 2033: 5e-05, 2046: 5e-05, 2047: 5e-05, 2048: 5e-05, 2049: 5e-05, 2050: 5e-05, 2051: 5e-05, 2052: 5e-05, 2053: 5e-05, 2054: 5e-05, 2055: 5e-05, 2056: 5e-05, 2058: 5e-05, 2071: 5e-05, 2072: 5e-05, 2074: 5e-05, 2075: 5e-05, 1842: 5e-05, 1843: 5e-05, 1844: 5e-05, 1845: 5e-05, 1847: 5e-05, 1848: 5e-05, 1885: 5e-05, 1886: 5e-05, 1887: 5e-05, 1888: 5e-05, 1889: 5e-05, 1890: 5e-05, 1891: 5e-05, 1892: 5e-05, 1893: 5e-05, 1927: 5e-05, 1930: 5e-05, 1931: 5e-05, 1934: 5e-05, 1799: 5e-05, 1804: 5e-05, 2108: 5e-05, 2109: 5e-05, 2110: 5e-05, 2111: 5e-05, 2112: 5e-05, 2121: 5e-05, 2122: 5e-05, 2123: 5e-05, 2124: 5e-05, 2125: 5e-05, 2126: 5e-05, 2127: 5e-05, 2128: 5e-05, 2136: 5e-05, 2137: 5e-05, 2138: 5e-05, 2139: 5e-05, 2140: 5e-05, 2141: 5e-05, 2142: 5e-05, 2143: 5e-05, 2151: 5e-05, 2154: 5e-05, 2155: 5e-05, 2156: 5e-05, 2158: 5e-05, 2159: 5e-05, 2160: 5e-05, 2161: 5e-05, 2168: 5e-05, 2170: 5e-05, 1765: 5e-05, 1766: 5e-05, 1768: 5e-05, 1769: 5e-05, 1770: 5e-05, 1806: 5e-05, 1809: 5e-05, 1810: 5e-05, 1811: 5e-05, 1812: 5e-05, 1813: 5e-05, 1814: 5e-05, 1815: 5e-05, 1816: 5e-05, 1817: 5e-05, 1818: 5e-05, 1819: 5e-05, 1821: 5e-05, 1858: 5e-05, 1861: 5e-05, 1862: 5e-05, 1865: 5e-05, 1752: 5e-05, 1839: 5e-05, 1884: 5e-05, 1707: 5e-05, 1708: 5e-05, 1709: 5e-05, 1710: 5e-05, 1820: 5e-05, 1822: 5e-05, 1823: 5e-05, 1824: 5e-05, 1825: 5e-05, 1826: 5e-05, 1827: 5e-05, 1828: 5e-05, 1829: 5e-05, 1830: 5e-05, 1831: 5e-05, 1870: 5e-05, 1873: 5e-05, 1874: 5e-05, 1875: 5e-05, 1876: 5e-05, 1877: 5e-05, 1878: 5e-05, 1879: 5e-05, 1880: 5e-05, 1881: 5e-05, 1882: 5e-05, 1883: 5e-05, 1921: 5e-05, 1924: 5e-05, 1925: 5e-05, 1926: 5e-05, 1802: 5e-05, 1803: 5e-05, 1897: 5e-05, 1900: 5e-05, 1903: 5e-05, 1759: 5e-05, 1760: 5e-05, 1798: 5e-05, 1801: 5e-05, 1856: 5e-05, 1995: 5e-05, 1999: 5e-05, 2000: 5e-05, 2003: 5e-05, 2004: 5e-05, 2007: 5e-05, 2031: 5e-05, 2032: 5e-05, 2034: 5e-05, 2035: 5e-05, 2036: 5e-05, 2037: 5e-05, 2038: 5e-05, 2039: 5e-05, 2040: 5e-05, 2041: 5e-05, 2042: 5e-05, 2043: 5e-05, 2044: 5e-05, 2045: 5e-05, 2064: 5e-05, 2067: 5e-05, 2068: 5e-05, 2069: 5e-05, 2070: 5e-05, 2091: 5e-05, 1846: 5e-05, 1849: 5e-05, 1852: 5e-05, 2145: 5e-05, 2148: 5e-05, 2149: 5e-05, 2150: 5e-05, 2152: 5e-05, 2153: 5e-05, 2157: 5e-05, 2162: 5e-05, 2163: 5e-05, 2164: 5e-05, 2165: 5e-05, 2166: 5e-05, 2167: 5e-05, 2169: 5e-05, 2171: 5e-05, 2172: 5e-05, 2173: 5e-05, 2174: 5e-05, 2175: 5e-05, 2176: 5e-05, 2177: 5e-05, 2178: 5e-05, 2179: 5e-05, 2180: 5e-05, 2181: 5e-05, 2182: 5e-05, 2183: 5e-05, 2184: 5e-05, 2185: 5e-05, 2186: 5e-05, 2187: 5e-05, 1793: 5e-05, 1795: 5e-05, 1796: 5e-05, 1840: 5e-05, 1841: 5e-05, 1807: 5e-05, 1853: 5e-05, 1854: 5e-05, 1805: 5e-05, 1808: 5e-05, 1850: 5e-05, 1851: 5e-05, 1855: 5e-05, 1857: 5e-05, 1859: 5e-05, 1860: 5e-05, 1864: 5e-05, 1901: 5e-05, 1904: 5e-05, 1894: 5e-05, 1895: 5e-05, 1896: 5e-05, 1898: 5e-05, 1899: 5e-05, 1935: 5e-05, 1936: 5e-05, 1938: 5e-05, 1939: 5e-05, 1940: 5e-05, 1941: 5e-05, 1942: 5e-05, 1943: 5e-05, 1944: 5e-05, 1945: 5e-05, 1949: 5e-05, 1982: 5e-05, 1985: 5e-05, 1986: 5e-05, 1987: 5e-05, 1989: 5e-05, 1992: 5e-05, 1697: 5e-05, 1698: 5e-05, 1702: 5e-05, 1751: 5e-05, 1753: 5e-05, 1755: 5e-05, 1756: 5e-05, 1794: 5e-05, 1797: 5e-05, 1800: 5e-05, 1754: 5e-05, 1757: 5e-05, 1758: 5e-05, 1761: 5e-05, 1762: 5e-05, 1763: 5e-05, 1764: 5e-05, 1767: 5e-05, 4: 5e-05, 2073: 5e-05, 2076: 5e-05, 2077: 5e-05, 2094: 5e-05, 2095: 5e-05, 2096: 5e-05, 2097: 5e-05, 2098: 5e-05, 2101: 5e-05, 2113: 5e-05, 2114: 5e-05, 2115: 5e-05, 2116: 5e-05, 2117: 5e-05, 2118: 5e-05, 2119: 5e-05, 2120: 5e-05, 2129: 5e-05, 2130: 5e-05, 2131: 5e-05, 2132: 5e-05, 2133: 5e-05, 2134: 5e-05, 2135: 5e-05, 2144: 5e-05, 2146: 5e-05, 2147: 5e-05, 1019: 0.0001, 1021: 0.0001, 1026: 0.0001, 1066: 0.0001, 1191: 0.0001, 1321: 0.0001, 1322: 0.0001, 1323: 0.0001, 1324: 0.0001, 1325: 0.0001, 1326: 0.0001, 1327: 0.0001, 1423: 0.0001, 1424: 0.0001, 1425: 0.0001, 1426: 0.0001, 1427: 0.0001, 1428: 0.0001, 1429: 0.0001, 1430: 0.0001, 1431: 0.0001, 1432: 0.0001, 1433: 0.0001, 1434: 0.0001, 1436: 0.0001, 1530: 0.0001, 1531: 0.0001, 1532: 0.0001, 1533: 0.0001, 1534: 0.0001, 1535: 0.0001, 1536: 0.0001, 1537: 0.0001, 1538: 0.0001, 1623: 0.0001, 1625: 0.0001, 1626: 0.0001, 2057: 5e-05, 2059: 5e-05, 2060: 5e-05, 2061: 5e-05, 2062: 5e-05, 2063: 5e-05, 2065: 5e-05, 2066: 5e-05, 2078: 5e-05, 2079: 5e-05, 2080: 5e-05, 2081: 5e-05, 2082: 5e-05, 2083: 5e-05, 2084: 5e-05, 2085: 5e-05, 2086: 5e-05, 2087: 5e-05, 2088: 5e-05, 2089: 5e-05, 2090: 5e-05, 2092: 5e-05, 2093: 5e-05, 2099: 5e-05, 2100: 5e-05, 2102: 5e-05, 2103: 5e-05, 2104: 5e-05, 2105: 5e-05, 2106: 5e-05, 2107: 5e-05, 1863: 5e-05, 1866: 5e-05, 1867: 5e-05, 1868: 5e-05, 1869: 5e-05, 1871: 5e-05, 1872: 5e-05, 1908: 5e-05, 1909: 5e-05, 1910: 5e-05, 1911: 5e-05, 1912: 5e-05, 1913: 5e-05, 1914: 5e-05, 1915: 5e-05, 1916: 5e-05, 1917: 5e-05, 1918: 5e-05, 1919: 5e-05, 1920: 5e-05, 1922: 5e-05, 1923: 5e-05, 1954: 5e-05, 1955: 5e-05, 1956: 5e-05, 1957: 5e-05, 1958: 5e-05, 1959: 5e-05, 1960: 5e-05, 1961: 5e-05, 1962: 5e-05, 1963: 5e-05, 1964: 5e-05, 1965: 5e-05, 1966: 5e-05, 1967: 5e-05, 1968: 5e-05, 1997: 5e-05, 1998: 5e-05, 2001: 5e-05, 2002: 5e-05, 2005: 5e-05, 2006: 5e-05, 602: 0.00067, 605: 0.00067, 663: 0.00067, 628: 0.00067, 660: 0.00067, 662: 0.00067, 585: 0.00067, 595: 0.00067, 614: 0.00067, 615: 0.00067, 616: 0.00067, 617: 0.00067, 618: 0.00067, 639: 0.00067, 603: 0.00067, 604: 0.00067, 661: 0.00067, 629: 0.00067, 630: 0.00067, 667: 0.00067, 634: 0.00067, 664: 0.00067, 607: 0.00067, 608: 0.00067, 633: 0.00067, 665: 0.00067, 591: 0.00067, 593: 0.00067, 594: 0.00067, 596: 0.00067, 609: 0.00067, 610: 0.00067, 613: 0.00067, 635: 0.00067, 638: 0.00067, 597: 0.00067, 598: 0.00067, 599: 0.00067, 611: 0.00067, 612: 0.00067, 636: 0.00067, 600: 0.00067, 625: 0.00067, 626: 0.00067, 586: 0.00067, 587: 0.00067, 588: 0.00067, 589: 0.00067, 590: 0.00067, 592: 0.00067, 606: 0.00067, 632: 0.00067, 601: 0.00067, 631: 0.00067, 1349: 0.00041, 1344: 0.00041, 1263: 0.00041, 1460: 0.00041, 1461: 0.00041, 1465: 0.00041, 1464: 0.00041, 1554: 0.00041, 1555: 0.00041, 1343: 0.00041, 1347: 0.00041, 1456: 0.00041, 1457: 0.00041, 1448: 0.00041, 1458: 0.00041, 1459: 0.00041, 1462: 0.00041, 1264: 0.00041, 1447: 0.00041, 1450: 0.00041, 1268: 0.00041, 1348: 0.00041, 1553: 0.00041, 1453: 0.00041, 1350: 0.00041, 1452: 0.00041, 1352: 0.00041, 1353: 0.00041, 1455: 0.00041, 1346: 0.00041, 1451: 0.00041, 1454: 0.00041, 812: 0.00017, 839: 0.00017, 848: 0.00017, 853: 0.00017, 805: 0.00017, 806: 0.00017, 893: 0.00017, 894: 0.00017, 813: 0.00017, 816: 0.00017, 846: 0.00017, 847: 0.00017, 850: 0.00017, 811: 0.00017, 814: 0.00017, 843: 0.00017, 809: 0.00017, 810: 0.00017, 807: 0.00017, 808: 0.00017, 838: 0.00017, 776: 0.00017, 777: 0.00017, 778: 0.00017, 815: 0.00017, 817: 0.00017, 851: 0.00017, 852: 0.00017, 854: 0.00017, 855: 0.00017, 856: 0.00017, 857: 0.00017, 892: 0.00017, 1776: 5e-05, 1777: 5e-05, 1832: 5e-05, 1833: 5e-05, 1773: 5e-05, 1721: 5e-05, 1771: 5e-05, 1772: 5e-05, 1592: 5e-05, 1659: 5e-05, 1662: 5e-05, 1723: 5e-05, 1780: 5e-05, 1781: 5e-05, 1782: 5e-05, 1785: 5e-05, 1834: 5e-05, 1835: 5e-05, 1836: 5e-05, 1837: 5e-05, 1599: 5e-05, 1668: 5e-05, 1669: 5e-05, 1671: 5e-05, 1674: 5e-05, 1732: 5e-05, 1733: 5e-05, 1588: 5e-05, 1653: 5e-05, 1655: 5e-05, 1658: 5e-05, 1719: 5e-05, 1725: 5e-05, 1726: 5e-05, 1729: 5e-05, 1730: 5e-05, 1774: 5e-05, 1775: 5e-05, 1778: 5e-05, 1779: 5e-05, 1591: 5e-05, 1660: 5e-05, 1661: 5e-05, 1663: 5e-05, 1666: 5e-05, 1724: 5e-05, 1727: 5e-05, 1673: 5e-05, 1678: 5e-05, 1735: 5e-05, 1736: 5e-05, 1737: 5e-05, 1738: 5e-05, 1739: 5e-05, 1741: 5e-05, 1742: 5e-05, 1587: 5e-05, 1656: 5e-05, 1657: 5e-05, 1720: 5e-05, 1783: 5e-05, 1784: 5e-05, 1786: 5e-05, 1787: 5e-05, 1788: 5e-05, 1789: 5e-05, 1790: 5e-05, 1792: 5e-05, 1838: 5e-05, 1664: 5e-05, 1665: 5e-05, 1667: 5e-05, 1670: 5e-05, 1728: 5e-05, 1731: 5e-05, 1734: 5e-05, 524: 0.00027, 522: 0.00027, 527: 0.00027, 521: 0.00027, 555: 0.00027, 556: 0.00027, 558: 0.00027, 561: 0.00027, 582: 0.00027, 583: 0.00027, 492: 0.00027, 491: 0.00027, 520: 0.00027, 178: 8e-05, 179: 8e-05, 180: 8e-05, 183: 8e-05, 68: 8e-05, 84: 8e-05, 107: 8e-05, 108: 8e-05, 110: 8e-05, 111: 8e-05, 109: 0.00339, 142: 0.00339, 143: 0.00339, 134: 8e-05, 177: 8e-05, 101: 8e-05, 103: 8e-05, 5: 8e-05, 6: 8e-05, 7: 8e-05, 8: 8e-05, 173: 8e-05, 174: 8e-05, 175: 8e-05, 176: 8e-05, 137: 8e-05, 181: 8e-05, 104: 8e-05, 105: 8e-05, 139: 8e-05, 102: 8e-05, 136: 8e-05, 138: 8e-05, 182: 8e-05, 187: 8e-05, 67: 8e-05, 69: 8e-05, 106: 8e-05, 184: 8e-05, 185: 8e-05, 186: 8e-05, 225: 8e-05, 33: 8e-05, 34: 8e-05, 35: 8e-05, 36: 8e-05, 40: 8e-05, 41: 8e-05, 42: 8e-05, 43: 8e-05, 47: 8e-05, 48: 8e-05, 49: 8e-05, 50: 8e-05, 51: 8e-05, 52: 8e-05, 53: 8e-05, 54: 8e-05, 63: 8e-05, 64: 8e-05, 65: 8e-05, 66: 8e-05, 133: 8e-05, 135: 8e-05, 144: 8e-05, 145: 8e-05, 140: 8e-05, 141: 8e-05, 1198: 0.01119, 1253: 0.01119, 1192: 0.01119, 1193: 0.01119, 1149: 0.01119, 1194: 0.01119, 2: 0.01119, 1147: 0.01119, 1150: 0.01119, 1195: 0.01119, 1104: 0.01119, 371: 0.00012, 372: 0.00012, 376: 0.00012, 514: 0.00012, 515: 0.00012, 546: 0.00012, 547: 0.00012, 416: 0.00012, 417: 0.00012, 451: 0.00012, 452: 0.00012, 453: 0.00012, 454: 0.00012, 457: 0.00012, 483: 0.00012, 544: 0.00012, 545: 0.00012, 549: 0.00012, 484: 0.00012, 486: 0.00012, 410: 0.00012, 411: 0.00012, 412: 0.00012, 413: 0.00012, 485: 0.00012, 513: 0.00012, 148: 0.00015, 153: 0.00015, 196: 0.00015, 149: 0.00015, 192: 0.00015, 193: 0.00015, 194: 0.00015, 195: 0.00015, 236: 0.00015, 124: 0.00015, 155: 0.00015, 114: 0.00015, 146: 0.00015, 156: 0.00015, 161: 0.00015, 202: 0.00015, 204: 0.00015, 207: 0.00015, 152: 0.00015, 157: 0.00015, 118: 0.00015, 147: 0.00015, 150: 0.00015, 151: 0.00015, 197: 0.00015, 198: 0.00015, 199: 0.00015, 239: 0.00015, 240: 0.00015, 241: 0.00015, 243: 0.00015, 244: 0.00015, 245: 0.00015, 246: 0.00015, 247: 0.00015, 250: 0.00015, 200: 0.00015, 201: 0.00015, 203: 0.00015, 83: 0.00015, 86: 0.00015, 112: 0.00015, 113: 0.00015, 115: 0.00015, 637: 0.00115, 670: 0.00115, 674: 0.00115, 675: 0.00115, 701: 0.00115, 668: 0.00115, 669: 0.00115, 725: 0.00115, 642: 0.00115, 672: 0.00115, 673: 0.00115, 696: 0.00115, 697: 0.00115, 703: 0.00115, 698: 0.00115, 699: 0.00115, 640: 0.00115, 641: 0.00115, 643: 0.00115, 644: 0.00115, 666: 0.00115, 671: 0.00115, 700: 0.00115, 722: 0.00115, 749: 0.00017, 750: 0.00017, 779: 0.00017, 780: 0.00017, 785: 0.00017, 788: 0.00017, 724: 0.00017, 748: 0.00017, 751: 0.00017, 715: 0.00017, 716: 0.00017, 744: 0.00017, 745: 0.00017, 746: 0.00017, 753: 0.00017, 758: 0.00017, 784: 0.00017, 786: 0.00017, 787: 0.00017, 789: 0.00017, 723: 0.00017, 752: 0.00017, 781: 0.00017, 782: 0.00017, 710: 0.00017, 711: 0.00017, 712: 0.00017, 754: 0.00017, 783: 0.00017, 1711: 0.00037, 1713: 0.00037, 1714: 0.00037, 1480: 0.00037, 1485: 0.00037, 1569: 0.00037, 1570: 0.00037, 1573: 0.00037, 1576: 0.00037, 1571: 0.00037, 1572: 0.00037, 1649: 0.00037, 1654: 0.00037, 1712: 0.00037, 1715: 0.00037, 1716: 0.00037, 1582: 0.00037, 1583: 0.00037, 1651: 0.00037, 1652: 0.00037, 1650: 0.00037, 1717: 0.00037, 1718: 0.00037, 1722: 0.00037, 1579: 0.00037, 1581: 0.00037, 1584: 0.00037, 1648: 0.00037, 1574: 0.00037, 1575: 0.00037, 1577: 0.00037, 1578: 0.00037, 1580: 0.00037, 1647: 0.00037, 227: 0.00013, 228: 0.00013, 229: 0.00013, 230: 0.00013, 274: 0.00013, 275: 0.00013, 302: 0.00013, 266: 0.00013, 267: 0.00013, 190: 0.00013, 191: 0.00013, 231: 0.00013, 232: 0.00013, 235: 0.00013, 242: 0.00013, 272: 0.00013, 273: 0.00013, 276: 0.00013, 226: 0.00013, 233: 0.00013, 234: 0.00013, 237: 0.00013, 238: 0.00013, 268: 0.00013, 269: 0.00013, 270: 0.00013, 271: 0.00013, 188: 0.00013, 189: 0.00013, 985: 0.00016, 987: 0.00016, 988: 0.00016, 1031: 0.00016, 1032: 0.00016, 1034: 0.00016, 1029: 0.00016, 1030: 0.00016, 1074: 0.00016, 1077: 0.00016, 944: 0.00016, 947: 0.00016, 978: 0.00016, 979: 0.00016, 981: 0.00016, 984: 0.00016, 919: 0.00016, 953: 0.00016, 954: 0.00016, 956: 0.00016, 957: 0.00016, 958: 0.00016, 959: 0.00016, 993: 0.00016, 1035: 0.00016, 1037: 0.00016, 1038: 0.00016, 1081: 0.00016, 1082: 0.00016, 937: 0.00016, 938: 0.00016, 939: 0.00016, 940: 0.00016, 941: 0.00016, 942: 0.00016, 943: 0.00016, 973: 0.00016, 974: 0.00016, 975: 0.00016, 977: 0.00016, 980: 0.00016, 983: 0.00016, 1020: 0.00016, 1023: 0.00016, 1024: 0.00016, 948: 0.00016, 949: 0.00016, 950: 0.00016, 951: 0.00016, 986: 0.00016, 995: 0.00016, 1000: 0.00016, 991: 0.00016, 994: 0.00016, 996: 0.00016, 1027: 0.00016, 1033: 0.02098, 1078: 0.02098, 1025: 0.00016, 1069: 0.00016, 1070: 0.00016, 1073: 0.00016, 952: 0.00016, 955: 0.00016, 989: 0.00016, 990: 0.00016, 992: 0.00016, 1028: 0.00016, 945: 0.00016, 946: 0.00016, 982: 0.00016, 73: 0.00025, 74: 0.00025, 121: 0.00025, 122: 0.00025, 154: 0.00025, 87: 0.00025, 88: 0.00025, 89: 0.00025, 91: 0.00025, 80: 0.00025, 81: 0.00025, 82: 0.00025, 37: 0.00025, 38: 0.00025, 39: 0.00025, 44: 0.00025, 85: 0.00025, 90: 0.00025, 70: 0.00025, 71: 0.00025, 72: 0.00025, 75: 0.00025, 0: 0.00025, 45: 0.00025, 55: 0.00025, 56: 0.00025, 76: 0.00025, 77: 0.00025, 119: 0.00025, 120: 0.00025, 78: 0.00025, 79: 0.00025, 116: 0.00025, 117: 0.00025, 690: 0.0005, 721: 0.0005, 717: 0.0005, 718: 0.0005, 686: 0.0005, 687: 0.0005, 691: 0.0005, 713: 0.0005, 714: 0.0005, 695: 0.0005, 719: 0.0005, 720: 0.0005, 747: 0.0005, 1091: 7e-05, 1134: 7e-05, 1041: 7e-05, 1044: 7e-05, 1086: 7e-05, 1089: 7e-05, 1090: 7e-05, 1093: 7e-05, 1184: 7e-05, 1186: 7e-05, 1228: 7e-05, 1231: 7e-05, 1092: 7e-05, 1140: 7e-05, 1141: 7e-05, 1176: 7e-05, 1135: 7e-05, 1136: 7e-05, 3: 7e-05, 1188: 7e-05, 1190: 7e-05, 1235: 7e-05, 1236: 7e-05, 1237: 7e-05, 1238: 7e-05, 1239: 7e-05, 1240: 7e-05, 1242: 7e-05, 1294: 7e-05, 999: 7e-05, 1036: 7e-05, 1039: 7e-05, 1042: 7e-05, 1003: 7e-05, 1004: 7e-05, 1040: 7e-05, 1043: 7e-05, 1005: 7e-05, 1006: 7e-05, 1007: 7e-05, 1045: 7e-05, 1046: 7e-05, 1047: 7e-05, 1048: 7e-05, 1049: 7e-05, 1050: 7e-05, 1051: 7e-05, 1052: 7e-05, 1144: 7e-05, 1145: 7e-05, 1181: 7e-05, 1183: 7e-05, 1131: 7e-05, 1132: 7e-05, 1137: 7e-05, 1171: 7e-05, 1172: 7e-05, 1173: 7e-05, 1174: 7e-05, 1175: 7e-05, 1178: 7e-05, 1220: 7e-05, 1084: 7e-05, 1127: 7e-05, 1128: 7e-05, 1130: 7e-05, 1133: 7e-05, 1168: 7e-05, 961: 7e-05, 962: 7e-05, 963: 7e-05, 964: 7e-05, 965: 7e-05, 997: 7e-05, 998: 7e-05, 1001: 7e-05, 1002: 7e-05, 1083: 7e-05, 1085: 7e-05, 1087: 7e-05, 1088: 7e-05, 1185: 7e-05, 1187: 7e-05, 1189: 7e-05, 1232: 7e-05, 1233: 7e-05, 1234: 7e-05, 1177: 7e-05, 1179: 7e-05, 1180: 7e-05, 1182: 7e-05, 1223: 7e-05, 1224: 7e-05, 1227: 7e-05, 1094: 7e-05, 1095: 7e-05, 1096: 7e-05, 1138: 7e-05, 1139: 7e-05, 1142: 7e-05, 1143: 7e-05, 285: 0.00012, 288: 0.00012, 253: 0.00012, 257: 0.00012, 206: 0.00012, 210: 0.00012, 211: 0.00012, 248: 0.00012, 251: 0.00012, 252: 0.00012, 304: 0.00012, 305: 0.00012, 307: 0.00012, 308: 0.00012, 311: 0.00012, 309: 0.00012, 277: 0.00012, 278: 0.00012, 281: 0.00012, 291: 0.00012, 292: 0.00012, 286: 0.00012, 289: 0.00012, 290: 0.00012, 279: 0.00012, 280: 0.00012, 284: 0.00012, 303: 0.00012, 306: 0.00012, 287: 0.00012, 310: 0.00012, 249: 0.00012, 254: 0.00012, 282: 0.00012, 283: 0.00012, 312: 0.00012, 313: 0.00012, 525: 0.00018, 534: 0.00018, 535: 0.00018, 539: 0.00018, 567: 0.00018, 570: 0.00018, 526: 0.00018, 559: 0.00018, 493: 0.00018, 496: 0.00018, 499: 0.00018, 528: 0.00018, 529: 0.00018, 497: 0.00018, 498: 0.00018, 503: 0.00018, 467: 0.00018, 471: 0.00018, 472: 0.00018, 500: 0.00018, 501: 0.00018, 504: 0.00018, 564: 0.00018, 565: 0.00018, 560: 0.00018, 562: 0.00018, 530: 0.00018, 531: 0.00018, 563: 0.00018, 502: 0.00018, 507: 0.00018, 532: 0.00018, 533: 0.00018, 536: 0.00018, 566: 0.00018, 568: 0.00018, 569: 0.00018, 572: 0.00018, 573: 0.00018, 494: 0.00018, 495: 0.00018, 13: 0.00275, 10: 0.00275, 11: 0.00275, 12: 0.00275, 18: 0.00275, 19: 0.00275, 20: 0.00275, 21: 0.00275, 22: 0.00275, 23: 0.00275, 24: 0.00275, 25: 0.00275, 26: 0.00275, 27: 0.00275, 28: 0.00275, 29: 0.00275, 30: 0.00275, 31: 0.00275, 32: 0.00275, 14: 0.00275, 9: 0.00275, 15: 0.00275, 16: 0.00275, 17: 0.00275, 657: 0.00339, 659: 0.00339, 688: 0.00339, 693: 0.00339, 658: 0.00339, 692: 0.00339, 656: 0.00339, 694: 0.00339, 689: 0.00339, 627: 0.00339, 92: 0.00021, 95: 0.00021, 98: 0.00021, 125: 0.00021, 96: 0.00021, 97: 0.00021, 99: 0.00021, 100: 0.00021, 128: 0.00021, 94: 0.00021, 93: 0.00021, 1204: 0.00214, 1112: 0.00214, 1114: 0.00214, 1117: 0.00214, 1155: 0.00214, 1153: 0.00214, 1205: 0.00214, 1158: 0.00214, 1258: 0.00214, 1203: 0.00214, 1206: 0.00214, 1201: 0.00214, 1157: 0.00214, 1261: 0.00214, 1200: 0.00214, 1156: 0.00214, 1159: 0.00214, 762: 0.00035, 726: 0.00035, 729: 0.00035, 728: 0.00035, 755: 0.00035, 727: 0.00035, 730: 0.00035, 731: 0.00035, 736: 0.00035, 756: 0.00035, 757: 0.00035, 759: 0.00035, 760: 0.00035, 761: 0.00035, 763: 0.00035, 765: 0.00035, 766: 0.00035, 732: 0.00035, 405: 6e-05, 406: 6e-05, 407: 6e-05, 408: 6e-05, 409: 6e-05, 445: 6e-05, 446: 6e-05, 319: 6e-05, 320: 6e-05, 321: 6e-05, 322: 6e-05, 323: 6e-05, 324: 6e-05, 325: 6e-05, 333: 6e-05, 334: 6e-05, 337: 6e-05, 473: 6e-05, 474: 6e-05, 342: 6e-05, 362: 6e-05, 364: 6e-05, 365: 6e-05, 367: 6e-05, 368: 6e-05, 438: 6e-05, 441: 6e-05, 442: 6e-05, 443: 6e-05, 444: 6e-05, 448: 6e-05, 338: 6e-05, 339: 6e-05, 340: 6e-05, 341: 6e-05, 343: 6e-05, 360: 6e-05, 361: 6e-05, 366: 6e-05, 369: 6e-05, 370: 6e-05, 399: 6e-05, 400: 6e-05, 401: 6e-05, 403: 6e-05, 404: 6e-05, 930: 0.00048, 1056: 0.00048, 1099: 0.00048, 1100: 0.00048, 1105: 0.00048, 1013: 0.00048, 1014: 0.00048, 1057: 0.00048, 1058: 0.00048, 1059: 0.00048, 1101: 0.00048, 1146: 0.00048, 972: 0.00048, 931: 0.00048, 1010: 0.00048, 966: 0.00048, 969: 0.00048, 970: 0.00048, 971: 0.00048, 976: 0.00048, 1008: 0.00048, 1009: 0.00048, 1011: 0.00048, 1103: 0.00048, 934: 0.00048, 935: 0.00048, 1055: 0.00048, 1060: 0.00048, 1053: 0.00048, 1054: 0.00048, 1097: 0.00048, 1102: 0.00048, 896: 0.00048, 1098: 0.00048, 968: 0.00048, 967: 0.00048, 1207: 0.00025, 1209: 0.00025, 1266: 0.00025, 1214: 0.00025, 1269: 0.00025, 1265: 0.00025, 1267: 0.00025, 1272: 0.00025, 1351: 0.00025, 1354: 0.00025, 1358: 0.00025, 1274: 0.00025, 1276: 0.00025, 1221: 0.00025, 1275: 0.00025, 1277: 0.00025, 1278: 0.00025, 1279: 0.00025, 1280: 0.00025, 1359: 0.00025, 1362: 0.00025, 1210: 0.00025, 1355: 0.00025, 1356: 0.00025, 1357: 0.00025, 1361: 0.00025, 1212: 0.00025, 1213: 0.00025, 1215: 0.00025, 1216: 0.00025, 1217: 0.00025, 1218: 0.00025, 1219: 0.00025, 1222: 0.00025, 1270: 0.00025, 1273: 0.00025, 1: 0.00012, 584: 0.00012, 580: 0.00012, 578: 0.00012, 579: 0.00012, 581: 0.00012, 548: 0.00012, 550: 0.00012, 551: 0.00012, 552: 0.00012, 553: 0.00012, 554: 0.00012, 557: 0.00012, 1151: 0.02098, 1152: 0.02098, 1199: 0.02098, 1154: 0.02098, 1196: 0.02098, 1257: 0.02098, 1061: 0.0001, 1062: 0.0001, 1063: 0.0001, 1202: 0.02098, 1197: 0.02098, 1254: 0.02098, 475: 5e-05, 476: 5e-05, 479: 5e-05, 505: 5e-05, 508: 5e-05, 509: 5e-05, 506: 5e-05, 510: 5e-05, 511: 5e-05, 537: 5e-05, 538: 5e-05, 540: 5e-05, 541: 5e-05, 542: 5e-05, 543: 5e-05, 571: 5e-05, 574: 5e-05, 575: 5e-05, 576: 5e-05, 577: 5e-05, 447: 5e-05, 449: 5e-05, 450: 5e-05, 477: 5e-05, 478: 5e-05, 480: 5e-05, 481: 5e-05, 482: 5e-05, 923: 0.00016, 925: 0.00016, 849: 0.00016, 888: 0.00016, 891: 0.00016, 921: 0.00016, 922: 0.00016, 924: 0.00016, 844: 0.00016, 886: 0.00016, 840: 0.00016, 842: 0.00016, 845: 0.00016, 890: 0.00016, 887: 0.00016, 889: 0.00016, 926: 0.00016, 927: 0.00016, 928: 0.00016, 929: 0.00016, 960: 0.00016, 623: 0.00012, 652: 0.00012, 645: 0.00012, 646: 0.00012, 647: 0.00012, 650: 0.00012, 651: 0.00012, 676: 0.00012, 677: 0.00012, 680: 0.00012, 681: 0.00012, 621: 0.00012, 648: 0.00012, 649: 0.00012, 619: 0.00012, 620: 0.00012, 622: 0.00012, 624: 0.00012, 678: 0.00012, 679: 0.00012, 683: 0.00012, 708: 0.00012, 709: 0.00012, 654: 0.00012, 655: 0.00012, 682: 0.00012, 684: 0.00012, 685: 0.00012, 653: 0.00012, 1292: 6e-05, 1371: 6e-05, 1372: 6e-05, 1374: 6e-05, 1377: 6e-05, 1386: 6e-05, 1387: 6e-05, 1388: 6e-05, 1389: 6e-05, 1393: 6e-05, 1490: 6e-05, 1491: 6e-05, 1492: 6e-05, 1380: 6e-05, 1382: 6e-05, 1383: 6e-05, 1385: 6e-05, 1381: 6e-05, 1479: 6e-05, 1482: 6e-05, 1290: 6e-05, 1291: 6e-05, 1293: 6e-05, 1295: 6e-05, 1296: 6e-05, 1378: 6e-05, 1379: 6e-05, 1483: 6e-05, 1484: 6e-05, 1486: 6e-05, 1489: 6e-05, 1384: 6e-05, 1487: 6e-05, 1488: 6e-05, 1493: 6e-05, 1375: 6e-05, 1376: 6e-05, 1241: 6e-05, 1243: 6e-05, 1245: 6e-05, 1297: 6e-05, 1298: 6e-05, 1299: 6e-05, 1300: 6e-05, 1301: 6e-05, 1304: 6e-05, 1244: 6e-05, 1302: 6e-05, 1303: 6e-05, 1305: 6e-05, 1308: 6e-05, 1390: 6e-05, 314: 0.00022, 329: 0.00022, 316: 0.00022, 317: 0.00022, 330: 0.00022, 326: 0.00022, 218: 0.00022, 221: 0.00022, 327: 0.00022, 328: 0.00022, 351: 0.00022, 297: 0.00022, 298: 0.00022, 299: 0.00022, 300: 0.00022, 301: 0.00022, 318: 0.00022, 220: 0.00022, 222: 0.00022, 223: 0.00022, 224: 0.00022, 260: 0.00022, 263: 0.00022, 264: 0.00022, 265: 0.00022, 258: 0.00022, 293: 0.00022, 294: 0.00022, 295: 0.00022, 296: 0.00022, 315: 0.00022, 332: 0.00022, 259: 0.00022, 261: 0.00022, 262: 0.00022, 1064: 0.0001, 1106: 0.0001, 1107: 0.0001, 1109: 0.0001, 1110: 0.0001, 1022: 0.0001, 1012: 0.0001, 1015: 0.0001, 1016: 0.0001, 1017: 0.0001, 1018: 0.0001, 1065: 0.0001, 1108: 0.0001, 1113: 0.0001, 1148: 0.0001, 1067: 0.0001, 1068: 0.0001, 1111: 0.0001}
prefecture_tile_dict = {'Aichi': [895, 865, 823, 
                                      866, 821, 825, 897, 46, 57, 58, 59, 60, 61, 62, 864, 869,
                                        862, 858, 859, 860, 818, 512, 824, 820, 861, 898, 899, 900, 932, 933, 936, 819, 402, 433, 434, 437, 516, 517, 518, 519, 523, 863, 822], 'Akita': [1512, 1513, 1517, 1605, 1601, 1602, 1603, 1604, 1607, 1608, 1672, 1675, 1400, 1499, 1502, 1503, 1505, 1506, 1313, 1314, 1317, 1399, 1402, 1403, 1404, 1405, 1408, 1409, 1413, 1507, 1510, 1511, 1514, 1312, 1315, 1310, 1394, 1395, 1396, 1397, 1398, 1401, 1392, 1494, 1495, 1496, 1497, 1498, 1585, 1586, 1504, 1508, 1509, 1593, 1594, 1595, 1596, 1597, 1598, 1600, 1500, 1501, 1589, 1590, 1306, 1307, 1309, 1311, 1391, 1316, 1318, 1320, 1406, 1407, 1410, 1411], 'Aomori': [1520, 1609, 1612, 1744, 1745, 1746, 1791, 1618, 1622, 1685, 1687, 1688, 1689, 1690, 1691, 1692, 1747, 1748, 1749, 1750, 1676, 1677, 1679, 1680, 1681, 1682, 1686, 1740, 1743, 1319, 1414, 1415, 1416, 1418, 1419, 1420, 1421, 1422, 1519, 1522, 1523, 1526, 1527, 1524, 1525, 1528, 1529, 1610, 1611, 1613, 1614, 1615, 1616, 1617, 1683, 1684, 1516, 1521, 1606, 1412, 1417, 1515, 1518], 'Chiba': [1260, 1246, 1248, 1336, 1341, 1446, 1271, 1345, 1337, 1338, 1259, 1342, 1251, 1249, 1250, 1252, 1255, 1340, 1256, 1335, 1334, 1552, 1449, 1247, 1339, 1445], 'Ehime': [460, 461, 487, 488, 489, 490, 347, 377, 418, 419, 420, 421, 422, 425, 455, 456, 458, 459, 378, 379, 381, 415, 423, 424, 426, 346, 348, 349, 350, 382, 383, 384, 386, 387, 344, 345, 373, 374, 375, 380, 414], 'Fukui': [735, 737, 739, 764, 767, 702, 704, 705, 706, 707, 733, 734, 797, 798, 799, 801, 802, 803, 804, 834, 835, 743, 771, 774, 775, 738, 740, 768, 769, 770, 741, 742, 772, 773], 'Fukuoka': [162, 165, 158, 213, 215, 160, 123, 214, 256, 255, 127, 163, 171, 216, 217, 219, 166, 172, 131, 167, 1262, 170, 205, 208, 209, 168, 164, 169, 212, 159, 126, 129, 130, 132], 'Fukushima': [1475, 1476, 1478, 1368, 1369, 1470, 1467, 1468, 1469, 1567, 1646, 1556, 1557, 1559, 1560, 1472, 1473, 1558, 1561, 1562, 1564, 1360, 1363, 1364, 1365, 1366, 1463, 1466, 1474, 1477, 1563, 1568, 1643, 1644, 1645, 1328, 1329, 1330, 1331, 1332, 1333, 1435, 1437, 1438, 1439, 1440, 1441, 1442, 1443, 1444, 1481, 1539, 1540, 1541, 1542, 1543, 1544, 1565, 1566, 1630, 1631, 1632, 1633, 1636, 1695, 1696, 1699, 1225, 1226, 1229, 1230, 1281, 1282, 1283, 1284, 1285, 1286, 1287, 1288, 1289, 1367, 1370, 1373, 1471], 'Gifu': [790, 791, 793, 878, 880, 881, 913, 914, 915, 916, 917, 920, 867, 829, 903, 907, 908, 912, 828, 868, 901, 871, 872, 873, 870, 826, 827, 836, 841, 879, 882, 883, 884, 885, 918, 794, 795, 796, 800, 830, 831, 832, 833, 837, 874, 875, 876, 877, 909, 910, 911, 902, 904, 905, 906, 792], 'Gunma': [1208, 1211, 1162, 1079, 1122, 1123, 1124, 1125, 1126, 1129, 1163, 1164, 1165, 1167, 1169, 1170, 1116, 1121, 1120, 1075, 1080, 1119, 1071, 1072, 1076, 1115, 1118, 1160, 1161, 1166], 'Hiroshima': [462, 388, 389, 390, 391, 464, 431, 432, 463, 465, 468, 402, 433, 434, 437, 516, 517, 518, 519, 523, 863, 435, 436, 439, 440, 466, 469, 470, 331, 336, 353, 427, 428, 429, 393, 394, 430, 335, 356, 357, 358, 359, 363, 392, 395, 396, 397, 398, 352, 354, 355, 385], 'Hokkaido': [1619, 1620, 1621, 1624, 1628, 1693, 1694, 1545, 1546, 1547, 1548, 1549, 1550, 1551, 1634, 1635, 1637, 1638, 1639, 1640, 1641, 1642, 1700, 1701, 1703, 1704, 1705, 1706, 1902, 1905, 1906, 1907, 1946, 1947, 1948, 1950, 1951, 1952, 1953, 1990, 1991, 1993, 1994, 1996, 1627, 1629, 1928, 1929, 1932, 1933, 1937, 1969, 1970, 1971, 1972, 1973, 1974, 1975, 1976, 1977, 1978, 1979, 1980, 1981, 1983, 1984, 1988, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025, 2026, 2027, 2028, 2029, 2030, 2033, 2046, 2047, 2048, 2049, 2050, 2051, 2052, 2053, 2054, 2055, 2056, 2058, 2071, 2072, 2074, 2075, 1842, 1843, 1844, 1845, 1847, 1848, 1885, 1886, 1887, 1888, 1889, 1890, 1891, 1892, 1893, 1927, 1930, 1931, 1934, 1799, 1804, 2108, 2109, 2110, 2111, 2112, 2121, 2122, 2123, 2124, 2125, 2126, 2127, 2128, 2136, 2137, 2138, 2139, 2140, 2141, 2142, 2143, 2151, 2154, 2155, 2156, 2158, 2159, 2160, 2161, 2168, 2170, 1765, 1766, 1768, 1769, 1770, 1806, 1809, 1810, 1811, 1812, 1813, 1814, 1815, 1816, 1817, 1818, 1819, 1821, 1858, 1861, 1862, 1865, 1752, 1839, 1884, 1707, 1708, 1709, 1710, 1820, 1822, 1823, 1824, 1825, 1826, 1827, 1828, 1829, 1830, 1831, 1870, 1873, 1874, 1875, 1876, 1877, 1878, 1879, 1880, 1881, 1882, 1883, 1921, 1924, 1925, 1926, 1802, 1803, 1897, 1900, 1903, 1759, 1760, 1798, 1801, 1856, 1995, 1999, 2000, 2003, 2004, 2007, 2031, 2032, 2034, 2035, 2036, 2037, 2038, 2039, 2040, 2041, 2042, 2043, 2044, 2045, 2064, 2067, 2068, 2069, 2070, 2091, 1846, 1849, 1852, 2145, 2148, 2149, 2150, 2152, 2153, 2157, 2162, 2163, 2164, 2165, 2166, 2167, 2169, 2171, 2172, 2173, 2174, 2175, 2176, 2177, 2178, 2179, 2180, 2181, 2182, 2183, 2184, 2185, 2186, 2187, 1793, 1795, 1796, 1840, 1841, 1807, 1853, 1854, 1805, 1808, 1850, 1851, 1855, 1857, 1859, 1860, 1864, 1901, 1904, 1894, 1895, 1896, 1898, 1899, 1935, 1936, 1938, 1939, 1940, 1941, 1942, 1943, 1944, 1945, 1949, 1982, 1985, 1986, 1987, 1989, 1992, 1697, 1698, 1702, 1751, 1753, 1755, 1756, 1794, 1328, 1329, 1330, 1331, 1332, 1333, 1435, 1437, 1438, 1439, 1440, 1441, 1442, 1443, 1444, 1481, 1539, 1540, 1541, 1542, 1543, 1544, 1565, 1566, 1630, 1631, 1632, 1633, 1636, 1695, 1696, 1699, 1797, 1800, 1754, 1757, 1758, 1761, 1762, 1763, 1764, 1767, 4, 2073, 2076, 2077, 2094, 2095, 2096, 2097, 2098, 2101, 2113, 2114, 2115, 2116, 2117, 2118, 2119, 2120, 2129, 2130, 2131, 2132, 2133, 2134, 2135, 2144, 2146, 2147, 1019, 1021, 1026, 1066, 1191, 1321, 1322, 1323, 1324, 1325, 1326, 1327, 1423, 1424, 1425, 1426, 1427, 1428, 1429, 1430, 1431, 1432, 1433, 1434, 1436, 1530, 1531, 1532, 1533, 1534, 1535, 1536, 1537, 1538, 1623, 1625, 1626, 2057, 2059, 2060, 2061, 2062, 2063, 2065, 2066, 2078, 2079, 2080, 2081, 2082, 2083, 2084, 2085, 2086, 2087, 2088, 2089, 2090, 2092, 2093, 2099, 2100, 2102, 2103, 2104, 2105, 2106, 2107, 1863, 1866, 1867, 1868, 1869, 1871, 1872, 1908, 1909, 1910, 1911, 1912, 1913, 1914, 1915, 1916, 1917, 1918, 1919, 1920, 1922, 1923, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966, 1967, 1968, 1997, 1998, 2001, 2002, 2005, 2006], 'Hyogo': [602, 605, 663, 628, 660, 662, 585, 595, 614, 615, 616, 617, 618, 639, 603, 604, 661, 629, 630, 667, 634, 664, 607, 608, 633, 665, 591, 593, 594, 596, 609, 610, 613, 635, 638, 597, 598, 599, 611, 612, 636, 600, 625, 626, 586, 587, 588, 589, 590, 592, 606, 632, 601, 631], 'Ibaraki': [1349, 1344, 1263, 1460, 1461, 1465, 1464, 1554, 1555, 1343, 1347, 1456, 1457, 1448, 1458, 1459, 1462, 1264, 1447, 1450, 1268, 1348, 1553, 1453, 131, 167, 1262, 1350, 1452, 1352, 1353, 1455, 1346, 1451, 1454], 'Ishikawa': [812, 839, 848, 853, 805, 806, 893, 894, 813, 816, 846, 847, 850, 811, 814, 843, 809, 810, 807, 808, 838, 776, 777, 778, 815, 817, 851, 852, 854, 855, 856, 857, 892], 'Iwate': [1776, 1777, 1832, 1833, 1773, 1721, 1771, 1772, 1592, 1659, 1662, 1723, 1780, 1781, 1782, 1785, 1834, 1835, 1836, 1837, 1599, 1668, 1669, 1671, 1674, 1732, 1733, 1588, 1653, 1655, 1658, 1719, 1725, 1726, 1729, 1730, 1774, 1775, 1778, 1779, 1591, 1660, 1661, 1663, 1666, 1724, 1727, 1673, 1678, 1735, 1736, 1737, 1738, 1739, 1741, 1742, 1587, 1656, 1657, 1720, 1783, 1784, 1786, 1787, 1788, 1789, 1790, 1792, 1838, 1664, 1665, 1667, 1670, 1728, 1731, 1734], 'Kagawa': [524, 522, 527, 521, 555, 556, 558, 561, 582, 583, 492, 491, 520], 'Kagoshima': [178, 179, 180, 183, 68, 84, 107, 108, 110, 111, 109, 142, 143, 134, 177, 101, 103, 5, 6, 7, 8, 173, 174, 175, 176, 137, 181, 104, 105, 139, 102, 136, 138, 182, 187, 67, 69, 106, 184, 185, 186, 225, 33, 34, 35, 36, 40, 41, 42, 43, 47, 48, 49, 50, 51, 52, 53, 54, 63, 64, 65, 66, 133, 135, 144, 145, 140, 141], 'Kanagawa': [1198, 1253, 1192, 1193, 1149, 1194, 2, 1147, 1150, 1195, 1104], 'Kochi': [371, 372, 376, 514, 515, 546, 547, 416, 417, 451, 452, 453, 454, 457, 483, 544, 545, 549, 484, 486, 410, 411, 412, 413, 485, 513, 512], 'Kumamoto': [148, 153, 196, 149, 192, 193, 194, 195, 236, 124, 155, 114, 146, 156, 161, 202, 204, 207, 152, 157, 118, 147, 150, 151, 197, 198, 199, 239, 240, 241, 243, 244, 245, 246, 247, 250, 200, 201, 203, 83, 86, 112, 113, 115], 'Kyoto': [637, 670, 674, 675, 701, 668, 669, 725, 642, 672, 673, 696, 697, 703, 698, 699, 640, 641, 643, 644, 666, 671, 700, 722], 'Mie': [749, 750, 779, 780, 785, 788, 724, 748, 751, 715, 716, 744, 745, 746, 753, 758, 784, 786, 787, 789, 723, 752, 781, 782, 710, 711, 712, 754, 783], 'Miyagi': [1711, 1713, 1714, 1480, 1485, 1569, 1570, 1573, 1576, 1571, 1572, 1649, 1654, 1712, 1715, 1716, 1582, 1583, 1651, 1652, 1650, 1717, 1718, 1722, 1579, 1581, 1584, 1648, 1574, 1575, 1577, 1578, 1580, 1647], 'Miyazaki': [227, 228, 229, 230, 274, 275, 302, 266, 267, 190, 191, 231, 232, 235, 242, 272, 273, 276, 226, 233, 234, 237, 238, 268, 269, 270, 271, 188, 189], 'Nagano': [985, 987, 988, 1031, 1032, 1034, 1029, 1030, 1074, 1077, 944, 947, 978, 979, 981, 984, 919, 953, 954, 956, 957, 958, 959, 993, 1035, 1037, 1038, 1081, 1082, 937, 938, 939, 940, 941, 942, 943, 973, 974, 975, 977, 980, 983, 1020, 1023, 1024, 948, 949, 950, 951, 986, 995, 1000, 991, 994, 996, 1027, 1033, 1078, 1025, 1069, 1070, 1073, 952, 955, 989, 990, 992, 1028, 945, 946, 982], 'Nagasaki': [73, 74, 121, 122, 154, 87, 88, 89, 91, 46, 57, 58, 59, 60, 61, 62, 80, 81, 82, 37, 38, 39, 44, 85, 90, 70, 71, 72, 75, 0, 45, 55, 56, 76, 77, 119, 120, 78, 79, 116, 117], 'Nara': [690, 721, 717, 718, 686, 687, 691, 713, 714, 695, 719, 720, 747], 'Niigata': [1091, 1134, 1041, 1044, 1086, 1089, 1090, 1093, 1184, 1186, 1228, 1231, 1092, 1140, 1141, 1176, 1135, 1136, 3, 1188, 1190, 1235, 1236, 1237, 1238, 1239, 1240, 1242, 1294, 999, 1036, 1039, 1042, 1003, 1004, 1040, 1043, 1005, 1006, 1007, 1045, 1046, 1047, 1048, 1049, 1050, 1051, 1052, 1144, 1145, 1181, 1183, 1131, 1132, 1137, 1171, 1172, 1173, 1174, 1175, 1178, 1220, 1084, 1127, 1128, 1130, 1133, 1168, 961, 962, 963, 964, 965, 997, 998, 1001, 1002, 1083, 1085, 1087, 1088, 1185, 1187, 1189, 1232, 1233, 1234, 1177, 1179, 1180, 1182, 1223, 1224, 1227, 1094, 1095, 1096, 1138, 1139, 1142, 1143], 'Oita': [285, 288, 253, 257, 206, 210, 211, 248, 251, 252, 304, 305, 307, 308, 311, 309, 277, 278, 281, 291, 292, 286, 289, 290, 279, 280, 284, 303, 306, 287, 310, 249, 254, 282, 283, 312, 313], 'Okayama': [525, 534, 535, 539, 567, 570, 526, 559, 493, 496, 499, 528, 529, 497, 498, 503, 467, 471, 472, 500, 501, 504, 564, 565, 560, 562, 530, 531, 563, 502, 507, 532, 533, 536, 566, 568, 569, 572, 573, 494, 495], 'Okinawa': [13, 10, 11, 12, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 14, 9, 15, 16, 17], 'Osaka': [741, 742, 772, 773, 657, 659, 688, 109, 142, 143, 693, 658, 692, 656, 694, 689, 627], 'Saga': [92, 95, 98, 125, 96, 97, 99, 100, 128, 94, 93], 'Saitama': [1204, 1112, 1114, 1117, 1155, 1153, 1205, 1158, 1258, 1203, 1206, 1201, 1157, 1261, 1200, 1156, 1159], 'Shiga': [762, 726, 729, 728, 755, 727, 730, 731, 736, 756, 757, 759, 760, 761, 763, 765, 766, 732], 'Shimane': [405, 406, 407, 408, 409, 445, 446, 319, 320, 321, 322, 323, 324, 325, 333, 334, 337, 473, 474, 342, 362, 364, 365, 367, 368, 438, 441, 442, 443, 444, 448, 338, 339, 340, 341, 343, 360, 361, 366, 369, 370, 399, 400, 401, 403, 404], 'Shizuoka': [930, 1056, 1099, 1100, 1105, 1013, 1014, 1057, 1058, 1059, 1101, 1146, 972, 931, 1010, 966, 969, 970, 971, 976, 1008, 1009, 1011, 1103, 934, 935, 1055, 1060, 1053, 1054, 1097, 1102, 896, 1098, 968, 967], 'Tochigi': [1207, 1209, 1266, 1214, 1269, 1265, 1267, 1272, 1351, 1354, 1358, 1274, 1276, 1221, 1275, 1277, 1278, 1279, 1280, 1359, 1362, 1210, 1271, 1345, 1355, 1356, 1357, 1361, 1212, 1213, 1215, 1216, 1217, 1218, 1219, 1222, 1270, 1273], 'Tokushima': [1, 584, 580, 578, 579, 581, 548, 550, 551, 552, 553, 554, 557, 402, 433, 434, 437, 516, 517, 518, 519, 523, 863], 'Tokyo': [1151, 1152, 463, 465, 468, 1199, 1154, 1196, 1257, 1061, 1062, 1063, 1033, 1078, 1202, 1162, 1197, 1254], 'Tottori': [475, 476, 479, 505, 508, 509, 506, 510, 511, 537, 538, 540, 541, 542, 543, 571, 574, 575, 576, 577, 447, 449, 450, 477, 478, 480, 481, 482], 'Toyama': [923, 925, 849, 888, 891, 921, 922, 924, 844, 886, 840, 842, 845, 890, 887, 889, 926, 927, 928, 929, 960], 'Wakayama': [623, 652, 645, 646, 647, 650, 651, 676, 677, 680, 681, 621, 648, 649, 619, 620, 622, 624, 678, 679, 683, 708, 709, 654, 655, 682, 684, 685, 653], 'Yamagata': [1292, 1371, 1372, 1374, 1377, 1386, 1387, 1388, 1389, 1393, 1490, 1491, 1492, 1380, 1382, 1383, 1385, 1381, 1479, 1482, 1290, 1291, 1293, 1295, 1296, 1378, 1379, 1483, 1484, 1486, 1489, 1384, 1487, 1488, 1493, 1375, 1376, 1241, 1243, 1245, 1297, 1298, 1299, 1300, 1301, 1304, 1244, 1302, 1303, 1305, 1308, 1390], 'Yamaguchi': [314, 329, 316, 317, 330, 326, 218, 221, 327, 328, 351, 297, 298, 299, 300, 301, 318, 220, 222, 223, 224, 260, 263, 264, 265, 258, 293, 294, 295, 296, 315, 332, 259, 261, 262], 'Yamanashi': [1064, 1106, 1107, 1109, 1110, 1022, 1012, 1015, 1016, 1017, 1018, 1065, 1019, 1021, 1026, 1066, 1191, 1321, 1322, 1323, 1324, 1325, 1326, 1327, 1423, 1424, 1425, 1426, 1427, 1428, 1429, 1430, 1431, 1432, 1433, 1434, 1436, 1530, 1531, 1532, 1533, 1534, 1535, 1536, 1537, 1538, 1623, 1625, 1626, 1108, 1113, 1148, 1067, 1068, 1111, 1061, 1062, 1063]}
tile_dict = {0: (129.25787691957586, 33.310776473487095), 1: (134.51978606604433, 33.985266746280494), 2: (139.18033416720212, 35.334247291867285), 3: (139.18033416720212, 38.571800601275584), 4: (144.8932640976536, 43.02343640171199), 5: (130.3637006038438, 30.33826615071237), 6: (130.3637006038438, 30.473164205271054), 7: (130.51404086517147, 30.473164205271054), 8: (130.51404086517147, 30.33826615071237), 9: (127.4537937836438, 26.29607763643571), 10: (127.4537937836438, 26.43097569099439), 11: (127.60413404497147, 26.43097569099439), 12: (127.60413404497147, 26.29607763643571), 13: (127.75447430629914, 26.29607763643571), 14: (127.75447430629914, 26.43097569099439), 15: (127.90481456762683, 26.43097569099439), 16: (127.90481456762683, 26.29607763643571), 17: (127.75447430629914, 26.56587374555307), 18: (127.75447430629914, 26.700771800111752), 19: (127.90481456762683, 26.700771800111752), 20: (127.90481456762683, 26.56587374555307), 21: (128.0551548289545, 26.56587374555307), 22: (128.0551548289545, 26.700771800111752), 23: (128.20549509028217, 26.700771800111752), 24: (128.20549509028217, 26.56587374555307), 25: (128.0551548289545, 26.835669854670435), 26: (128.0551548289545, 26.970567909229114), 27: (128.20549509028217, 26.970567909229114), 28: (128.20549509028217, 26.835669854670435), 29: (128.35583535160984, 27.37526207290516), 30: (128.35583535160984, 27.510160127463838), 31: (128.5061756129375, 27.510160127463838), 32: (128.5061756129375, 27.37526207290516), 33: (128.65651587426518, 27.645058182022517), 34: (128.65651587426518, 27.7799562365812), 35: (128.80685613559285, 27.7799562365812), 36: (128.80685613559285, 27.645058182022517), 37: (128.65651587426518, 32.77118425525238), 38: (128.80685613559285, 32.90608230981106), 39: (128.80685613559285, 32.77118425525238), 40: (128.95719639692052, 28.18465040025724), 41: (128.95719639692052, 28.319548454815923), 42: (129.1075366582482, 28.319548454815923), 43: (129.1075366582482, 28.18465040025724), 44: (128.95719639692052, 33.040980364369744), 45: (128.95719639692052, 33.310776473487095), 46: (129.1075366582482, 34.25506285539785), 47: (129.25787691957586, 28.18465040025724), 48: (129.25787691957586, 28.319548454815923), 49: (129.40821718090353, 28.319548454815923), 50: (129.40821718090353, 28.18465040025724), 51: (129.25787691957586, 28.454446509374606), 52: (129.25787691957586, 28.589344563933285), 53: (129.40821718090353, 28.589344563933285), 54: (129.40821718090353, 28.454446509374606), 55: (129.40821718090353, 33.44567452804578), 56: (129.40821718090353, 33.310776473487095), 57: (129.25787691957586, 34.25506285539785), 58: (129.25787691957586, 34.38996090995653), 59: (129.25787691957586, 34.52485896451521), 60: (129.25787691957586, 34.65975701907389), 61: (129.40821718090353, 34.79465507363257), 62: (129.40821718090353, 34.65975701907389), 63: (129.5585574422312, 28.454446509374606), 64: (129.5585574422312, 28.589344563933285), 65: (129.70889770355888, 28.589344563933285), 66: (129.70889770355888, 28.454446509374606), 67: (129.5585574422312, 31.691999818782946), 68: (129.5585574422312, 31.826897873341625), 69: (129.70889770355888, 31.691999818782946), 70: (129.70889770355888, 32.90608230981106), 71: (129.70889770355888, 32.77118425525238), 72: (129.5585574422312, 33.040980364369744), 73: (129.5585574422312, 33.17587841892842), 74: (129.70889770355888, 33.17587841892842), 75: (129.70889770355888, 33.040980364369744), 76: (129.5585574422312, 33.310776473487095), 77: (129.5585574422312, 33.44567452804578), 78: (129.70889770355888, 33.44567452804578), 79: (129.70889770355888, 33.310776473487095), 80: (129.70889770355888, 33.58057258260446), 81: (129.5585574422312, 33.85036869172181), 82: (129.70889770355888, 33.85036869172181), 83: (130.00957822621422, 32.366490091576345), 84: (130.00957822621422, 32.23159203701766), 85: (130.00957822621422, 32.636286200693704), 86: (130.00957822621422, 32.50138814613503), 87: (129.85923796488655, 32.77118425525238), 88: (129.85923796488655, 32.90608230981106), 89: (130.00957822621422, 32.90608230981106), 90: (130.00957822621422, 32.77118425525238), 91: (129.85923796488655, 33.040980364369744), 92: (129.85923796488655, 33.17587841892842), 93: (130.00957822621422, 33.17587841892842), 94: (130.00957822621422, 33.040980364369744), 95: (129.85923796488655, 33.310776473487095), 96: (129.85923796488655, 33.44567452804578), 97: (130.00957822621422, 33.44567452804578), 98: (130.00957822621422, 33.310776473487095), 99: (129.85923796488655, 33.58057258260446), 100: (130.00957822621422, 33.58057258260446), 101: (130.1599184875419, 31.42220370966558), 102: (130.31025874886956, 31.557101764224264), 103: (130.31025874886956, 31.42220370966558), 104: (130.1599184875419, 31.826897873341625), 105: (130.31025874886956, 31.826897873341625), 106: (130.31025874886956, 31.691999818782946), 107: (130.1599184875419, 31.961795927900305), 108: (130.1599184875419, 32.09669398245899), 109: (130.31025874886956, 32.09669398245899), 110: (130.31025874886956, 31.961795927900305), 111: (130.1599184875419, 32.23159203701766), 112: (130.1599184875419, 32.366490091576345), 113: (130.31025874886956, 32.366490091576345), 114: (130.31025874886956, 32.23159203701766), 115: (130.1599184875419, 32.50138814613503), 116: (130.1599184875419, 32.636286200693704), 117: (130.31025874886956, 32.636286200693704), 118: (130.31025874886956, 32.50138814613503), 119: (130.1599184875419, 32.77118425525238), 120: (130.1599184875419, 32.90608230981106), 121: (130.31025874886956, 32.90608230981106), 122: (130.31025874886956, 32.77118425525238), 123: (130.31025874886956, 33.17587841892842), 124: (130.31025874886956, 33.040980364369744), 125: (130.1599184875419, 33.310776473487095), 126: (130.1599184875419, 33.44567452804578), 127: (130.31025874886956, 33.44567452804578), 128: (130.31025874886956, 33.310776473487095), 129: (130.1599184875419, 33.58057258260446), 130: (130.1599184875419, 33.715470637163136), 131: (130.31025874886956, 33.715470637163136), 132: (130.31025874886956, 33.58057258260446), 133: (130.46059901019723, 31.287305655106902), 134: (130.6109392715249, 31.152407600548223), 135: (130.46059901019723, 31.42220370966558), 136: (130.46059901019723, 31.557101764224264), 137: (130.6109392715249, 31.557101764224264), 138: (130.46059901019723, 31.691999818782946), 139: (130.46059901019723, 31.826897873341625), 140: (130.6109392715249, 31.826897873341625), 141: (130.6109392715249, 31.691999818782946), 142: (130.46059901019723, 31.961795927900305), 143: (130.46059901019723, 32.09669398245899), 144: (130.6109392715249, 32.09669398245899), 145: (130.6109392715249, 31.961795927900305), 146: (130.46059901019723, 32.23159203701766), 147: (130.46059901019723, 32.366490091576345), 148: (130.6109392715249, 32.366490091576345), 149: (130.6109392715249, 32.23159203701766), 150: (130.46059901019723, 32.50138814613503), 151: (130.46059901019723, 32.636286200693704), 152: (130.6109392715249, 32.636286200693704), 153: (130.6109392715249, 32.50138814613503), 154: (130.46059901019723, 32.77118425525238), 155: (130.46059901019723, 32.90608230981106), 156: (130.6109392715249, 32.90608230981106), 157: (130.6109392715249, 32.77118425525238), 158: (130.46059901019723, 33.040980364369744), 159: (130.46059901019723, 33.17587841892842), 160: (130.6109392715249, 33.17587841892842), 161: (130.6109392715249, 33.040980364369744), 162: (130.46059901019723, 33.310776473487095), 163: (130.46059901019723, 33.44567452804578), 164: (130.6109392715249, 33.44567452804578), 165: (130.6109392715249, 33.310776473487095), 166: (130.46059901019723, 33.58057258260446), 167: (130.46059901019723, 33.715470637163136), 168: (130.6109392715249, 33.715470637163136), 169: (130.6109392715249, 33.58057258260446), 170: (130.46059901019723, 33.85036869172181), 171: (130.6109392715249, 33.985266746280494), 172: (130.6109392715249, 33.85036869172181), 173: (130.76127953285257, 30.477917327754817), 174: (130.91161979418024, 30.477917327754817), 175: (130.91161979418024, 30.74771343687218), 176: (130.91161979418024, 30.6128153823135), 177: (130.76127953285257, 31.152407600548223), 178: (130.76127953285257, 31.287305655106902), 179: (130.91161979418024, 31.287305655106902), 180: (130.76127953285257, 31.42220370966558), 181: (130.76127953285257, 31.557101764224264), 182: (130.91161979418024, 31.557101764224264), 183: (130.91161979418024, 31.42220370966558), 184: (130.76127953285257, 31.691999818782946), 185: (130.76127953285257, 31.826897873341625), 186: (130.91161979418024, 31.826897873341625), 187: (130.91161979418024, 31.691999818782946), 188: (130.76127953285257, 31.961795927900305), 189: (130.76127953285257, 32.09669398245899), 190: (130.91161979418024, 32.09669398245899), 191: (130.91161979418024, 31.961795927900305), 192: (130.76127953285257, 32.23159203701766), 193: (130.76127953285257, 32.366490091576345), 194: (130.91161979418024, 32.366490091576345), 195: (130.91161979418024, 32.23159203701766), 196: (130.76127953285257, 32.50138814613503), 197: (130.76127953285257, 32.636286200693704), 198: (130.91161979418024, 32.636286200693704), 199: (130.91161979418024, 32.50138814613503), 200: (130.76127953285257, 32.77118425525238), 201: (130.76127953285257, 32.90608230981106), 202: (130.91161979418024, 32.90608230981106), 203: (130.91161979418024, 32.77118425525238), 204: (130.76127953285257, 33.040980364369744), 205: (130.76127953285257, 33.17587841892842), 206: (130.91161979418024, 33.17587841892842), 207: (130.91161979418024, 33.040980364369744), 208: (130.76127953285257, 33.310776473487095), 209: (130.76127953285257, 33.44567452804578), 210: (130.91161979418024, 33.44567452804578), 211: (130.91161979418024, 33.310776473487095), 212: (130.76127953285257, 33.58057258260446), 213: (130.76127953285257, 33.715470637163136), 214: (130.91161979418024, 33.715470637163136), 215: (130.91161979418024, 33.58057258260446), 216: (130.76127953285257, 33.85036869172181), 217: (130.76127953285257, 33.985266746280494), 218: (130.91161979418024, 33.985266746280494), 219: (130.91161979418024, 33.85036869172181), 220: (130.91161979418024, 34.25506285539785), 221: (130.91161979418024, 34.12016480083918), 222: (130.76127953285257, 34.38996090995653), 223: (130.91161979418024, 34.52485896451521), 224: (130.91161979418024, 34.38996090995653), 225: (131.0619600555079, 31.557101764224264), 226: (131.21230031683558, 31.557101764224264), 227: (131.0619600555079, 31.691999818782946), 228: (131.0619600555079, 31.826897873341625), 229: (131.21230031683558, 31.826897873341625), 230: (131.21230031683558, 31.691999818782946), 231: (131.0619600555079, 31.961795927900305), 232: (131.0619600555079, 32.09669398245899), 233: (131.21230031683558, 32.09669398245899), 234: (131.21230031683558, 31.961795927900305), 235: (131.0619600555079, 32.23159203701766), 236: (131.0619600555079, 32.366490091576345), 237: (131.21230031683558, 32.366490091576345), 238: (131.21230031683558, 32.23159203701766), 239: (131.0619600555079, 32.50138814613503), 240: (131.0619600555079, 32.636286200693704), 241: (131.21230031683558, 32.636286200693704), 242: (131.21230031683558, 32.50138814613503), 243: (131.0619600555079, 32.77118425525238), 244: (131.0619600555079, 32.90608230981106), 245: (131.21230031683558, 32.90608230981106), 246: (131.21230031683558, 32.77118425525238), 247: (131.0619600555079, 33.040980364369744), 248: (131.0619600555079, 33.17587841892842), 249: (131.21230031683558, 33.17587841892842), 250: (131.21230031683558, 33.040980364369744), 251: (131.0619600555079, 33.310776473487095), 252: (131.0619600555079, 33.44567452804578), 253: (131.21230031683558, 33.44567452804578), 254: (131.21230031683558, 33.310776473487095), 255: (131.0619600555079, 33.58057258260446), 256: (131.0619600555079, 33.715470637163136), 257: (131.21230031683558, 33.58057258260446), 258: (131.21230031683558, 33.985266746280494), 259: (131.0619600555079, 34.12016480083918), 260: (131.0619600555079, 34.25506285539785), 261: (131.21230031683558, 34.25506285539785), 262: (131.21230031683558, 34.12016480083918), 263: (131.0619600555079, 34.38996090995653), 264: (131.21230031683558, 34.52485896451521), 265: (131.21230031683558, 34.38996090995653), 266: (131.36264057816325, 31.691999818782946), 267: (131.36264057816325, 31.826897873341625), 268: (131.36264057816325, 31.961795927900305), 269: (131.36264057816325, 32.09669398245899), 270: (131.36264057816325, 32.23159203701766), 271: (131.36264057816325, 32.366490091576345), 272: (131.51298083949092, 32.366490091576345), 273: (131.36264057816325, 32.50138814613503), 274: (131.36264057816325, 32.636286200693704), 275: (131.51298083949092, 32.636286200693704), 276: (131.51298083949092, 32.50138814613503), 277: (131.36264057816325, 32.77118425525238), 278: (131.36264057816325, 32.90608230981106), 279: (131.51298083949092, 32.90608230981106), 280: (131.51298083949092, 32.77118425525238), 281: (131.36264057816325, 33.040980364369744), 282: (131.36264057816325, 33.17587841892842), 283: (131.51298083949092, 33.17587841892842), 284: (131.51298083949092, 33.040980364369744), 285: (131.36264057816325, 33.310776473487095), 286: (131.36264057816325, 33.44567452804578), 287: (131.51298083949092, 33.44567452804578), 288: (131.51298083949092, 33.310776473487095), 289: (131.36264057816325, 33.58057258260446), 290: (131.36264057816325, 33.715470637163136), 291: (131.51298083949092, 33.715470637163136), 292: (131.51298083949092, 33.58057258260446), 293: (131.36264057816325, 34.12016480083918), 294: (131.36264057816325, 34.25506285539785), 295: (131.51298083949092, 34.25506285539785), 296: (131.51298083949092, 34.12016480083918), 297: (131.36264057816325, 34.38996090995653), 298: (131.36264057816325, 34.52485896451521), 299: (131.51298083949092, 34.52485896451521), 300: (131.51298083949092, 34.38996090995653), 301: (131.51298083949092, 34.65975701907389), 302: (131.6633211008186, 32.77118425525238), 303: (131.6633211008186, 32.90608230981106), 304: (131.81366136214626, 32.90608230981106), 305: (131.81366136214626, 32.77118425525238), 306: (131.6633211008186, 33.040980364369744), 307: (131.6633211008186, 33.17587841892842), 308: (131.81366136214626, 33.17587841892842), 309: (131.81366136214626, 33.040980364369744), 310: (131.6633211008186, 33.310776473487095), 311: (131.81366136214626, 33.310776473487095), 312: (131.6633211008186, 33.58057258260446), 313: (131.6633211008186, 33.715470637163136), 314: (131.6633211008186, 34.12016480083918), 315: (131.6633211008186, 34.25506285539785), 316: (131.81366136214626, 34.25506285539785), 317: (131.81366136214626, 34.12016480083918), 318: (131.6633211008186, 34.38996090995653), 319: (131.6633211008186, 34.52485896451521), 320: (131.81366136214626, 34.52485896451521), 321: (131.81366136214626, 34.38996090995653), 322: (131.6633211008186, 34.65975701907389), 323: (131.6633211008186, 34.79465507363257), 324: (131.81366136214626, 34.79465507363257), 325: (131.81366136214626, 34.65975701907389), 326: (131.96400162347393, 33.985266746280494), 327: (132.1143418848016, 33.985266746280494), 328: (132.1143418848016, 33.85036869172181), 329: (131.96400162347393, 34.12016480083918), 330: (131.96400162347393, 34.25506285539785), 331: (132.1143418848016, 34.25506285539785), 332: (132.1143418848016, 34.12016480083918), 333: (131.96400162347393, 34.38996090995653), 334: (131.96400162347393, 34.52485896451521), 335: (132.1143418848016, 34.52485896451521), 336: (132.1143418848016, 34.38996090995653), 337: (131.96400162347393, 34.65975701907389), 338: (131.96400162347393, 34.79465507363257), 339: (132.1143418848016, 34.79465507363257), 340: (132.1143418848016, 34.65975701907389), 341: (131.96400162347393, 34.929553128191245), 342: (132.1143418848016, 35.06445118274993), 343: (132.1143418848016, 34.929553128191245), 344: (132.41502240745695, 33.17587841892842), 345: (132.41502240745695, 33.040980364369744), 346: (132.41502240745695, 33.44567452804578), 347: (132.41502240745695, 33.310776473487095), 348: (132.26468214612927, 33.58057258260446), 349: (132.41502240745695, 33.715470637163136), 350: (132.41502240745695, 33.58057258260446), 351: (132.26468214612927, 33.985266746280494), 352: (132.41502240745695, 33.985266746280494), 353: (132.26468214612927, 34.25506285539785), 354: (132.41502240745695, 34.25506285539785), 355: (132.41502240745695, 34.12016480083918), 356: (132.26468214612927, 34.38996090995653), 357: (132.26468214612927, 34.52485896451521), 358: (132.41502240745695, 34.52485896451521), 359: (132.41502240745695, 34.38996090995653), 360: (132.26468214612927, 34.65975701907389), 361: (132.26468214612927, 34.79465507363257), 362: (132.41502240745695, 34.79465507363257), 363: (132.41502240745695, 34.65975701907389), 364: (132.26468214612927, 34.929553128191245), 365: (132.26468214612927, 35.06445118274993), 366: (132.41502240745695, 35.06445118274993), 367: (132.41502240745695, 34.929553128191245), 368: (132.26468214612927, 35.19934923730861), 369: (132.41502240745695, 35.334247291867285), 370: (132.41502240745695, 35.19934923730861), 371: (132.56536266878462, 32.90608230981106), 372: (132.7157029301123, 32.90608230981106), 373: (132.56536266878462, 33.040980364369744), 374: (132.56536266878462, 33.17587841892842), 375: (132.7157029301123, 33.17587841892842), 376: (132.7157029301123, 33.040980364369744), 377: (132.56536266878462, 33.310776473487095), 378: (132.56536266878462, 33.44567452804578), 379: (132.7157029301123, 33.44567452804578), 380: (132.7157029301123, 33.310776473487095), 381: (132.56536266878462, 33.58057258260446), 382: (132.56536266878462, 33.715470637163136), 383: (132.7157029301123, 33.715470637163136), 384: (132.7157029301123, 33.58057258260446), 385: (132.56536266878462, 33.985266746280494), 386: (132.7157029301123, 33.985266746280494), 387: (132.7157029301123, 33.85036869172181), 388: (132.56536266878462, 34.25506285539785), 389: (132.7157029301123, 34.25506285539785), 390: (132.7157029301123, 34.12016480083918), 391: (132.56536266878462, 34.38996090995653), 392: (132.56536266878462, 34.52485896451521), 393: (132.7157029301123, 34.52485896451521), 394: (132.7157029301123, 34.38996090995653), 395: (132.56536266878462, 34.65975701907389), 396: (132.56536266878462, 34.79465507363257), 397: (132.7157029301123, 34.79465507363257), 398: (132.7157029301123, 34.65975701907389), 399: (132.56536266878462, 34.929553128191245), 400: (132.56536266878462, 35.06445118274993), 401: (132.7157029301123, 35.06445118274993), 402: (132.7157029301123, 34.929553128191245), 403: (132.56536266878462, 35.19934923730861), 404: (132.56536266878462, 35.334247291867285), 405: (132.7157029301123, 35.334247291867285), 406: (132.7157029301123, 35.19934923730861), 407: (132.56536266878462, 35.46914534642596), 408: (132.7157029301123, 35.604043400984644), 409: (132.7157029301123, 35.46914534642596), 410: (132.86604319143996, 32.90608230981106), 411: (132.86604319143996, 33.040980364369744), 412: (132.86604319143996, 33.17587841892842), 413: (133.01638345276763, 33.17587841892842), 414: (132.86604319143996, 33.310776473487095), 415: (132.86604319143996, 33.44567452804578), 416: (133.01638345276763, 33.44567452804578), 417: (133.01638345276763, 33.310776473487095), 418: (132.86604319143996, 33.58057258260446), 419: (132.86604319143996, 33.715470637163136), 420: (133.01638345276763, 33.715470637163136), 421: (133.01638345276763, 33.58057258260446), 422: (132.86604319143996, 33.85036869172181), 423: (132.86604319143996, 33.985266746280494), 424: (133.01638345276763, 33.985266746280494), 425: (133.01638345276763, 33.85036869172181), 426: (132.86604319143996, 34.12016480083918), 427: (132.86604319143996, 34.25506285539785), 428: (133.01638345276763, 34.25506285539785), 429: (132.86604319143996, 34.38996090995653), 430: (132.86604319143996, 34.52485896451521), 431: (133.01638345276763, 34.52485896451521), 432: (133.01638345276763, 34.38996090995653), 433: (132.86604319143996, 34.65975701907389), 434: (132.86604319143996, 34.79465507363257), 435: (133.01638345276763, 34.79465507363257), 436: (133.01638345276763, 34.65975701907389), 437: (132.86604319143996, 34.929553128191245), 438: (132.86604319143996, 35.06445118274993), 439: (133.01638345276763, 35.06445118274993), 440: (133.01638345276763, 34.929553128191245), 441: (132.86604319143996, 35.19934923730861), 442: (132.86604319143996, 35.334247291867285), 443: (133.01638345276763, 35.334247291867285), 444: (133.01638345276763, 35.19934923730861), 445: (132.86604319143996, 35.46914534642596), 446: (132.86604319143996, 35.604043400984644), 447: (133.01638345276763, 35.604043400984644), 448: (133.01638345276763, 35.46914534642596), 449: (132.86604319143996, 36.14363561921936), 450: (133.01638345276763, 36.14363561921936), 451: (133.1667237140953, 33.310776473487095), 452: (133.1667237140953, 33.44567452804578), 453: (133.31706397542297, 33.44567452804578), 454: (133.1667237140953, 33.58057258260446), 455: (133.1667237140953, 33.715470637163136), 456: (133.31706397542297, 33.715470637163136), 457: (133.31706397542297, 33.58057258260446), 458: (133.1667237140953, 33.85036869172181), 459: (133.1667237140953, 33.985266746280494), 460: (133.31706397542297, 33.985266746280494), 461: (133.31706397542297, 33.85036869172181), 462: (133.1667237140953, 34.38996090995653), 463: (133.1667237140953, 34.52485896451521), 464: (133.31706397542297, 34.52485896451521), 465: (133.1667237140953, 34.65975701907389), 466: (133.1667237140953, 34.79465507363257), 467: (133.31706397542297, 34.79465507363257), 468: (133.31706397542297, 34.65975701907389), 469: (133.1667237140953, 34.929553128191245), 470: (133.1667237140953, 35.06445118274993), 471: (133.31706397542297, 35.06445118274993), 472: (133.31706397542297, 34.929553128191245), 473: (133.1667237140953, 35.19934923730861), 474: (133.1667237140953, 35.334247291867285), 475: (133.31706397542297, 35.334247291867285), 476: (133.31706397542297, 35.19934923730861), 477: (133.1667237140953, 35.46914534642596), 478: (133.1667237140953, 35.604043400984644), 479: (133.31706397542297, 35.46914534642596), 480: (133.1667237140953, 36.27853367377804), 481: (133.1667237140953, 36.41343172833672), 482: (133.31706397542297, 36.27853367377804), 483: (133.46740423675064, 33.58057258260446), 484: (133.46740423675064, 33.715470637163136), 485: (133.6177444980783, 33.715470637163136), 486: (133.6177444980783, 33.58057258260446), 487: (133.46740423675064, 33.85036869172181), 488: (133.46740423675064, 33.985266746280494), 489: (133.6177444980783, 33.985266746280494), 490: (133.6177444980783, 33.85036869172181), 491: (133.6177444980783, 34.25506285539785), 492: (133.6177444980783, 34.12016480083918), 493: (133.46740423675064, 34.52485896451521), 494: (133.6177444980783, 34.52485896451521), 495: (133.6177444980783, 34.38996090995653), 496: (133.46740423675064, 34.65975701907389), 497: (133.46740423675064, 34.79465507363257), 498: (133.6177444980783, 34.79465507363257), 499: (133.6177444980783, 34.65975701907389), 500: (133.46740423675064, 34.929553128191245), 501: (133.46740423675064, 35.06445118274993), 502: (133.6177444980783, 35.06445118274993), 503: (133.6177444980783, 34.929553128191245), 504: (133.46740423675064, 35.19934923730861), 505: (133.46740423675064, 35.334247291867285), 506: (133.6177444980783, 35.334247291867285), 507: (133.6177444980783, 35.19934923730861), 508: (133.46740423675064, 35.46914534642596), 509: (133.46740423675064, 35.604043400984644), 510: (133.6177444980783, 35.604043400984644), 511: (133.6177444980783, 35.46914534642596), 512: (133.76808475940598, 33.58057258260446), 513: (133.76808475940598, 33.715470637163136), 514: (133.91842502073365, 33.715470637163136), 515: (133.91842502073365, 33.58057258260446), 516: (133.76808475940598, 33.85036869172181), 517: (133.76808475940598, 33.985266746280494), 518: (133.91842502073365, 33.985266746280494), 519: (133.91842502073365, 33.85036869172181), 520: (133.76808475940598, 34.12016480083918), 521: (133.76808475940598, 34.25506285539785), 522: (133.91842502073365, 34.25506285539785), 523: (133.91842502073365, 34.12016480083918), 524: (133.76808475940598, 34.38996090995653), 525: (133.76808475940598, 34.52485896451521), 526: (133.91842502073365, 34.52485896451521), 527: (133.91842502073365, 34.38996090995653), 528: (133.76808475940598, 34.65975701907389), 529: (133.76808475940598, 34.79465507363257), 530: (133.91842502073365, 34.79465507363257), 531: (133.91842502073365, 34.65975701907389), 532: (133.76808475940598, 34.929553128191245), 533: (133.76808475940598, 35.06445118274993), 534: (133.91842502073365, 35.06445118274993), 535: (133.91842502073365, 34.929553128191245), 536: (133.76808475940598, 35.19934923730861), 537: (133.76808475940598, 35.334247291867285), 538: (133.91842502073365, 35.334247291867285), 539: (133.91842502073365, 35.19934923730861), 540: (133.76808475940598, 35.46914534642596), 541: (133.76808475940598, 35.604043400984644), 542: (133.91842502073365, 35.604043400984644), 543: (133.91842502073365, 35.46914534642596), 544: (134.06876528206132, 33.310776473487095), 545: (134.06876528206132, 33.44567452804578), 546: (134.06876528206132, 33.58057258260446), 547: (134.06876528206132, 33.715470637163136), 548: (134.219105543389, 33.715470637163136), 549: (134.219105543389, 33.58057258260446), 550: (134.06876528206132, 33.85036869172181), 551: (134.06876528206132, 33.985266746280494), 552: (134.219105543389, 33.985266746280494), 553: (134.219105543389, 33.85036869172181), 554: (134.06876528206132, 34.12016480083918), 555: (134.06876528206132, 34.25506285539785), 556: (134.219105543389, 34.25506285539785), 557: (134.219105543389, 34.12016480083918), 558: (134.06876528206132, 34.38996090995653), 559: (134.06876528206132, 34.52485896451521), 560: (134.219105543389, 34.52485896451521), 561: (134.219105543389, 34.38996090995653), 562: (134.06876528206132, 34.65975701907389), 563: (134.06876528206132, 34.79465507363257), 564: (134.219105543389, 34.79465507363257), 565: (134.219105543389, 34.65975701907389), 566: (134.06876528206132, 34.929553128191245), 567: (134.06876528206132, 35.06445118274993), 568: (134.219105543389, 35.06445118274993), 569: (134.219105543389, 34.929553128191245), 570: (134.06876528206132, 35.19934923730861), 571: (134.06876528206132, 35.334247291867285), 572: (134.219105543389, 35.334247291867285), 573: (134.219105543389, 35.19934923730861), 574: (134.06876528206132, 35.46914534642596), 575: (134.06876528206132, 35.604043400984644), 576: (134.219105543389, 35.604043400984644), 577: (134.219105543389, 35.46914534642596), 578: (134.36944580471666, 33.85036869172181), 579: (134.36944580471666, 33.985266746280494), 580: (134.51978606604433, 33.85036869172181), 581: (134.36944580471666, 34.12016480083918), 582: (134.36944580471666, 34.25506285539785), 583: (134.51978606604433, 34.25506285539785), 584: (134.51978606604433, 34.12016480083918), 585: (134.36944580471666, 34.929553128191245), 586: (134.36944580471666, 35.06445118274993), 587: (134.51978606604433, 35.06445118274993), 588: (134.51978606604433, 34.929553128191245), 589: (134.36944580471666, 35.19934923730861), 590: (134.36944580471666, 35.334247291867285), 591: (134.51978606604433, 35.334247291867285), 592: (134.51978606604433, 35.19934923730861), 593: (134.36944580471666, 35.46914534642596), 594: (134.36944580471666, 35.604043400984644), 595: (134.51978606604433, 35.604043400984644), 596: (134.51978606604433, 35.46914534642596), 597: (134.670126327372, 34.25506285539785), 598: (134.670126327372, 34.38996090995653), 599: (134.670126327372, 34.52485896451521), 600: (134.82046658869967, 34.52485896451521), 601: (134.82046658869967, 34.38996090995653), 602: (134.670126327372, 34.79465507363257), 603: (134.82046658869967, 34.79465507363257), 604: (134.82046658869967, 34.65975701907389), 605: (134.670126327372, 34.929553128191245), 606: (134.670126327372, 35.06445118274993), 607: (134.82046658869967, 35.06445118274993), 608: (134.82046658869967, 34.929553128191245), 609: (134.670126327372, 35.19934923730861), 610: (134.670126327372, 35.334247291867285), 611: (134.82046658869967, 35.334247291867285), 612: (134.82046658869967, 35.19934923730861), 613: (134.670126327372, 35.46914534642596), 614: (134.670126327372, 35.604043400984644), 615: (134.82046658869967, 35.604043400984644), 616: (134.82046658869967, 35.46914534642596), 617: (134.670126327372, 35.738941455543326), 618: (134.82046658869967, 35.738941455543326), 619: (134.97080685002734, 33.985266746280494), 620: (135.12114711135501, 33.985266746280494), 621: (135.12114711135501, 33.85036869172181), 622: (134.97080685002734, 34.12016480083918), 623: (135.12114711135501, 34.25506285539785), 624: (135.12114711135501, 34.12016480083918), 625: (134.97080685002734, 34.38996090995653), 626: (134.97080685002734, 34.52485896451521), 627: (135.12114711135501, 34.38996090995653), 628: (134.97080685002734, 34.65975701907389), 629: (134.97080685002734, 34.79465507363257), 630: (135.12114711135501, 34.79465507363257), 631: (134.97080685002734, 34.929553128191245), 632: (134.97080685002734, 35.06445118274993), 633: (135.12114711135501, 35.06445118274993), 634: (135.12114711135501, 34.929553128191245), 635: (134.97080685002734, 35.19934923730861), 636: (134.97080685002734, 35.334247291867285), 637: (135.12114711135501, 35.334247291867285), 638: (135.12114711135501, 35.19934923730861), 639: (134.97080685002734, 35.46914534642596), 640: (134.97080685002734, 35.604043400984644), 641: (135.12114711135501, 35.604043400984644), 642: (135.12114711135501, 35.46914534642596), 643: (134.97080685002734, 35.738941455543326), 644: (135.12114711135501, 35.738941455543326), 645: (135.27148737268269, 33.715470637163136), 646: (135.42182763401036, 33.715470637163136), 647: (135.42182763401036, 33.58057258260446), 648: (135.27148737268269, 33.85036869172181), 649: (135.27148737268269, 33.985266746280494), 650: (135.42182763401036, 33.985266746280494), 651: (135.42182763401036, 33.85036869172181), 652: (135.27148737268269, 34.12016480083918), 653: (135.27148737268269, 34.25506285539785), 654: (135.42182763401036, 34.25506285539785), 655: (135.42182763401036, 34.12016480083918), 656: (135.27148737268269, 34.38996090995653), 657: (135.27148737268269, 34.52485896451521), 658: (135.42182763401036, 34.52485896451521), 659: (135.42182763401036, 34.38996090995653), 660: (135.27148737268269, 34.65975701907389), 661: (135.27148737268269, 34.79465507363257), 662: (135.42182763401036, 34.79465507363257), 663: (135.42182763401036, 34.65975701907389), 664: (135.27148737268269, 34.929553128191245), 665: (135.27148737268269, 35.06445118274993), 666: (135.42182763401036, 35.06445118274993), 667: (135.42182763401036, 34.929553128191245), 668: (135.27148737268269, 35.19934923730861), 669: (135.27148737268269, 35.334247291867285), 670: (135.42182763401036, 35.334247291867285), 671: (135.42182763401036, 35.19934923730861), 672: (135.27148737268269, 35.46914534642596), 673: (135.27148737268269, 35.604043400984644), 674: (135.42182763401036, 35.604043400984644), 675: (135.42182763401036, 35.46914534642596), 676: (135.57216789533803, 33.58057258260446), 677: (135.57216789533803, 33.715470637163136), 678: (135.7225081566657, 33.715470637163136), 679: (135.7225081566657, 33.58057258260446), 680: (135.57216789533803, 33.85036869172181), 681: (135.57216789533803, 33.985266746280494), 682: (135.7225081566657, 33.985266746280494), 683: (135.7225081566657, 33.85036869172181), 684: (135.57216789533803, 34.12016480083918), 685: (135.57216789533803, 34.25506285539785), 686: (135.7225081566657, 34.25506285539785), 687: (135.7225081566657, 34.12016480083918), 688: (135.57216789533803, 34.38996090995653), 689: (135.57216789533803, 34.52485896451521), 690: (135.7225081566657, 34.52485896451521), 691: (135.7225081566657, 34.38996090995653), 692: (135.57216789533803, 34.65975701907389), 693: (135.57216789533803, 34.79465507363257), 694: (135.7225081566657, 34.79465507363257), 695: (135.7225081566657, 34.65975701907389), 696: (135.57216789533803, 34.929553128191245), 697: (135.57216789533803, 35.06445118274993), 698: (135.7225081566657, 35.06445118274993), 699: (135.7225081566657, 34.929553128191245), 700: (135.57216789533803, 35.19934923730861), 701: (135.57216789533803, 35.334247291867285), 702: (135.7225081566657, 35.334247291867285), 703: (135.7225081566657, 35.19934923730861), 704: (135.57216789533803, 35.46914534642596), 705: (135.57216789533803, 35.604043400984644), 706: (135.7225081566657, 35.604043400984644), 707: (135.7225081566657, 35.46914534642596), 708: (135.87284841799337, 33.715470637163136), 709: (135.87284841799337, 33.85036869172181), 710: (135.87284841799337, 33.985266746280494), 711: (136.02318867932104, 33.985266746280494), 712: (136.02318867932104, 33.85036869172181), 713: (135.87284841799337, 34.12016480083918), 714: (135.87284841799337, 34.25506285539785), 715: (136.02318867932104, 34.25506285539785), 716: (136.02318867932104, 34.12016480083918), 717: (135.87284841799337, 34.38996090995653), 718: (135.87284841799337, 34.52485896451521), 719: (136.02318867932104, 34.52485896451521), 720: (136.02318867932104, 34.38996090995653), 721: (135.87284841799337, 34.65975701907389), 722: (135.87284841799337, 34.79465507363257), 723: (136.02318867932104, 34.79465507363257), 724: (136.02318867932104, 34.65975701907389), 725: (135.87284841799337, 34.929553128191245), 726: (135.87284841799337, 35.06445118274993), 727: (136.02318867932104, 35.06445118274993), 728: (136.02318867932104, 34.929553128191245), 729: (135.87284841799337, 35.19934923730861), 730: (135.87284841799337, 35.334247291867285), 731: (136.02318867932104, 35.334247291867285), 732: (136.02318867932104, 35.19934923730861), 733: (135.87284841799337, 35.46914534642596), 734: (135.87284841799337, 35.604043400984644), 735: (136.02318867932104, 35.604043400984644), 736: (136.02318867932104, 35.46914534642596), 737: (135.87284841799337, 35.738941455543326), 738: (136.02318867932104, 35.873839510102), 739: (136.02318867932104, 35.738941455543326), 740: (135.87284841799337, 36.00873756466068), 741: (135.87284841799337, 36.14363561921936), 742: (136.02318867932104, 36.14363561921936), 743: (136.02318867932104, 36.00873756466068), 744: (136.1735289406487, 34.12016480083918), 745: (136.1735289406487, 34.25506285539785), 746: (136.32386920197638, 34.25506285539785), 747: (136.1735289406487, 34.38996090995653), 748: (136.1735289406487, 34.52485896451521), 749: (136.32386920197638, 34.52485896451521), 750: (136.32386920197638, 34.38996090995653), 751: (136.1735289406487, 34.65975701907389), 752: (136.1735289406487, 34.79465507363257), 753: (136.32386920197638, 34.79465507363257), 754: (136.32386920197638, 34.65975701907389), 755: (136.1735289406487, 34.929553128191245), 756: (136.1735289406487, 35.06445118274993), 757: (136.32386920197638, 35.06445118274993), 758: (136.32386920197638, 34.929553128191245), 759: (136.1735289406487, 35.19934923730861), 760: (136.1735289406487, 35.334247291867285), 761: (136.32386920197638, 35.334247291867285), 762: (136.32386920197638, 35.19934923730861), 763: (136.1735289406487, 35.46914534642596), 764: (136.1735289406487, 35.604043400984644), 765: (136.32386920197638, 35.604043400984644), 766: (136.32386920197638, 35.46914534642596), 767: (136.1735289406487, 35.738941455543326), 768: (136.1735289406487, 35.873839510102), 769: (136.32386920197638, 35.873839510102), 770: (136.32386920197638, 35.738941455543326), 771: (136.1735289406487, 36.00873756466068), 772: (136.1735289406487, 36.14363561921936), 773: (136.32386920197638, 36.14363561921936), 774: (136.32386920197638, 36.00873756466068), 775: (136.1735289406487, 36.27853367377804), 776: (136.1735289406487, 36.41343172833672), 777: (136.32386920197638, 36.41343172833672), 778: (136.32386920197638, 36.27853367377804), 779: (136.47420946330405, 34.38996090995653), 780: (136.47420946330405, 34.52485896451521), 781: (136.62454972463172, 34.52485896451521), 782: (136.62454972463172, 34.38996090995653), 783: (136.47420946330405, 34.65975701907389), 784: (136.47420946330405, 34.79465507363257), 785: (136.62454972463172, 34.65975701907389), 786: (136.47420946330405, 34.929553128191245), 787: (136.47420946330405, 35.06445118274993), 788: (136.62454972463172, 35.06445118274993), 789: (136.47420946330405, 35.19934923730861), 790: (136.47420946330405, 35.334247291867285), 791: (136.62454972463172, 35.334247291867285), 792: (136.62454972463172, 35.19934923730861), 793: (136.47420946330405, 35.46914534642596), 794: (136.47420946330405, 35.604043400984644), 795: (136.62454972463172, 35.604043400984644), 796: (136.62454972463172, 35.46914534642596), 797: (136.47420946330405, 35.738941455543326), 798: (136.47420946330405, 35.873839510102), 799: (136.62454972463172, 35.873839510102), 800: (136.62454972463172, 35.738941455543326), 801: (136.47420946330405, 36.00873756466068), 802: (136.47420946330405, 36.14363561921936), 803: (136.62454972463172, 36.14363561921936), 804: (136.62454972463172, 36.00873756466068), 805: (136.47420946330405, 36.27853367377804), 806: (136.47420946330405, 36.41343172833672), 807: (136.62454972463172, 36.41343172833672), 808: (136.62454972463172, 36.27853367377804), 809: (136.47420946330405, 36.548329782895394), 810: (136.47420946330405, 36.683227837454076), 811: (136.62454972463172, 36.683227837454076), 812: (136.62454972463172, 36.548329782895394), 813: (136.62454972463172, 36.953023946571435), 814: (136.62454972463172, 36.81812589201276), 815: (136.62454972463172, 37.22282005568879), 816: (136.62454972463172, 37.08792200113011), 817: (136.62454972463172, 37.357718110247475), 818: (136.7748899859594, 34.929553128191245), 819: (136.7748899859594, 35.06445118274993), 820: (136.92523024728706, 35.06445118274993), 821: (136.92523024728706, 34.929553128191245), 822: (136.7748899859594, 35.19934923730861), 823: (136.7748899859594, 35.334247291867285), 824: (136.92523024728706, 35.334247291867285), 825: (136.92523024728706, 35.19934923730861), 826: (136.7748899859594, 35.46914534642596), 827: (136.7748899859594, 35.604043400984644), 828: (136.92523024728706, 35.604043400984644), 829: (136.92523024728706, 35.46914534642596), 830: (136.7748899859594, 35.738941455543326), 831: (136.7748899859594, 35.873839510102), 832: (136.92523024728706, 35.873839510102), 833: (136.92523024728706, 35.738941455543326), 834: (136.7748899859594, 36.00873756466068), 835: (136.7748899859594, 36.14363561921936), 836: (136.92523024728706, 36.14363561921936), 837: (136.92523024728706, 36.00873756466068), 838: (136.7748899859594, 36.27853367377804), 839: (136.7748899859594, 36.41343172833672), 840: (136.92523024728706, 36.41343172833672), 841: (136.92523024728706, 36.27853367377804), 842: (136.7748899859594, 36.548329782895394), 843: (136.7748899859594, 36.683227837454076), 844: (136.92523024728706, 36.683227837454076), 845: (136.92523024728706, 36.548329782895394), 846: (136.7748899859594, 36.81812589201276), 847: (136.7748899859594, 36.953023946571435), 848: (136.92523024728706, 36.953023946571435), 849: (136.92523024728706, 36.81812589201276), 850: (136.7748899859594, 37.08792200113011), 851: (136.7748899859594, 37.22282005568879), 852: (136.92523024728706, 37.22282005568879), 853: (136.92523024728706, 37.08792200113011), 854: (136.7748899859594, 37.357718110247475), 855: (136.7748899859594, 37.49261616480615), 856: (136.92523024728706, 37.49261616480615), 857: (136.92523024728706, 37.357718110247475), 858: (137.07557050861473, 34.65975701907389), 859: (137.07557050861473, 34.79465507363257), 860: (137.2259107699424, 34.79465507363257), 861: (137.2259107699424, 34.65975701907389), 862: (137.07557050861473, 34.929553128191245), 863: (137.07557050861473, 35.06445118274993), 864: (137.2259107699424, 35.06445118274993), 865: (137.2259107699424, 34.929553128191245), 866: (137.07557050861473, 35.19934923730861), 867: (137.07557050861473, 35.334247291867285), 868: (137.2259107699424, 35.334247291867285), 869: (137.2259107699424, 35.19934923730861), 870: (137.07557050861473, 35.46914534642596), 871: (137.07557050861473, 35.604043400984644), 872: (137.2259107699424, 35.604043400984644), 873: (137.2259107699424, 35.46914534642596), 874: (137.07557050861473, 35.738941455543326), 875: (137.07557050861473, 35.873839510102), 876: (137.2259107699424, 35.873839510102), 877: (137.2259107699424, 35.738941455543326), 878: (137.07557050861473, 36.00873756466068), 879: (137.07557050861473, 36.14363561921936), 880: (137.2259107699424, 36.14363561921936), 881: (137.2259107699424, 36.00873756466068), 882: (137.07557050861473, 36.27853367377804), 883: (137.07557050861473, 36.41343172833672), 884: (137.2259107699424, 36.41343172833672), 885: (137.2259107699424, 36.27853367377804), 886: (137.07557050861473, 36.548329782895394), 887: (137.07557050861473, 36.683227837454076), 888: (137.2259107699424, 36.683227837454076), 889: (137.2259107699424, 36.548329782895394), 890: (137.07557050861473, 36.81812589201276), 891: (137.2259107699424, 36.81812589201276), 892: (137.07557050861473, 37.357718110247475), 893: (137.07557050861473, 37.49261616480615), 894: (137.2259107699424, 37.49261616480615), 895: (137.37625103127007, 34.79465507363257), 896: (137.52659129259774, 34.79465507363257), 897: (137.37625103127007, 34.929553128191245), 898: (137.37625103127007, 35.06445118274993), 899: (137.52659129259774, 35.06445118274993), 900: (137.52659129259774, 34.929553128191245), 901: (137.37625103127007, 35.19934923730861), 902: (137.37625103127007, 35.334247291867285), 903: (137.52659129259774, 35.334247291867285), 904: (137.52659129259774, 35.19934923730861), 905: (137.37625103127007, 35.46914534642596), 906: (137.37625103127007, 35.604043400984644), 907: (137.52659129259774, 35.604043400984644), 908: (137.52659129259774, 35.46914534642596), 909: (137.37625103127007, 35.738941455543326), 910: (137.37625103127007, 35.873839510102), 911: (137.52659129259774, 35.873839510102), 912: (137.52659129259774, 35.738941455543326), 913: (137.37625103127007, 36.00873756466068), 914: (137.37625103127007, 36.14363561921936), 915: (137.52659129259774, 36.14363561921936), 916: (137.52659129259774, 36.00873756466068), 917: (137.37625103127007, 36.27853367377804), 918: (137.37625103127007, 36.41343172833672), 919: (137.52659129259774, 36.41343172833672), 920: (137.52659129259774, 36.27853367377804), 921: (137.37625103127007, 36.548329782895394), 922: (137.37625103127007, 36.683227837454076), 923: (137.52659129259774, 36.683227837454076), 924: (137.52659129259774, 36.548329782895394), 925: (137.37625103127007, 36.81812589201276), 926: (137.37625103127007, 36.953023946571435), 927: (137.52659129259774, 36.953023946571435), 928: (137.52659129259774, 36.81812589201276), 929: (137.52659129259774, 37.08792200113011), 930: (137.6769315539254, 34.79465507363257), 931: (137.82727181525308, 34.79465507363257), 932: (137.6769315539254, 34.929553128191245), 933: (137.6769315539254, 35.06445118274993), 934: (137.82727181525308, 35.06445118274993), 935: (137.82727181525308, 34.929553128191245), 936: (137.6769315539254, 35.19934923730861), 937: (137.6769315539254, 35.334247291867285), 938: (137.82727181525308, 35.334247291867285), 939: (137.82727181525308, 35.19934923730861), 940: (137.6769315539254, 35.46914534642596), 941: (137.6769315539254, 35.604043400984644), 942: (137.82727181525308, 35.604043400984644), 943: (137.82727181525308, 35.46914534642596), 944: (137.6769315539254, 35.738941455543326), 945: (137.6769315539254, 35.873839510102), 946: (137.82727181525308, 35.873839510102), 947: (137.82727181525308, 35.738941455543326), 948: (137.6769315539254, 36.00873756466068), 949: (137.6769315539254, 36.14363561921936), 950: (137.82727181525308, 36.14363561921936), 951: (137.82727181525308, 36.00873756466068), 952: (137.6769315539254, 36.27853367377804), 953: (137.6769315539254, 36.41343172833672), 954: (137.82727181525308, 36.41343172833672), 955: (137.82727181525308, 36.27853367377804), 956: (137.6769315539254, 36.548329782895394), 957: (137.6769315539254, 36.683227837454076), 958: (137.82727181525308, 36.683227837454076), 959: (137.82727181525308, 36.548329782895394), 960: (137.6769315539254, 36.81812589201276), 961: (137.6769315539254, 36.953023946571435), 962: (137.82727181525308, 36.953023946571435), 963: (137.82727181525308, 36.81812589201276), 964: (137.6769315539254, 37.08792200113011), 965: (137.82727181525308, 37.08792200113011), 966: (137.97761207658075, 34.79465507363257), 967: (138.12795233790843, 34.79465507363257), 968: (138.12795233790843, 34.65975701907389), 969: (137.97761207658075, 34.929553128191245), 970: (137.97761207658075, 35.06445118274993), 971: (138.12795233790843, 35.06445118274993), 972: (138.12795233790843, 34.929553128191245), 973: (137.97761207658075, 35.19934923730861), 974: (137.97761207658075, 35.334247291867285), 975: (138.12795233790843, 35.334247291867285), 976: (138.12795233790843, 35.19934923730861), 977: (137.97761207658075, 35.46914534642596), 978: (137.97761207658075, 35.604043400984644), 979: (138.12795233790843, 35.604043400984644), 980: (138.12795233790843, 35.46914534642596), 981: (137.97761207658075, 35.738941455543326), 982: (137.97761207658075, 35.873839510102), 983: (138.12795233790843, 35.873839510102), 984: (138.12795233790843, 35.738941455543326), 985: (137.97761207658075, 36.00873756466068), 986: (137.97761207658075, 36.14363561921936), 987: (138.12795233790843, 36.14363561921936), 988: (138.12795233790843, 36.00873756466068), 989: (137.97761207658075, 36.27853367377804), 990: (137.97761207658075, 36.41343172833672), 991: (138.12795233790843, 36.41343172833672), 992: (138.12795233790843, 36.27853367377804), 993: (137.97761207658075, 36.548329782895394), 994: (137.97761207658075, 36.683227837454076), 995: (138.12795233790843, 36.683227837454076), 996: (138.12795233790843, 36.548329782895394), 997: (137.97761207658075, 36.81812589201276), 998: (137.97761207658075, 36.953023946571435), 999: (138.12795233790843, 36.953023946571435), 1000: (138.12795233790843, 36.81812589201276), 1001: (137.97761207658075, 37.08792200113011), 1002: (137.97761207658075, 37.22282005568879), 1003: (138.12795233790843, 37.22282005568879), 1004: (138.12795233790843, 37.08792200113011), 1005: (138.12795233790843, 38.03220838304087), 1006: (138.12795233790843, 37.89731032848219), 1007: (138.12795233790843, 38.16710643759954), 1008: (138.2782925992361, 34.929553128191245), 1009: (138.2782925992361, 35.06445118274993), 1010: (138.42863286056377, 35.06445118274993), 1011: (138.2782925992361, 35.19934923730861), 1012: (138.2782925992361, 35.334247291867285), 1013: (138.42863286056377, 35.334247291867285), 1014: (138.42863286056377, 35.19934923730861), 1015: (138.2782925992361, 35.46914534642596), 1016: (138.2782925992361, 35.604043400984644), 1017: (138.42863286056377, 35.604043400984644), 1018: (138.42863286056377, 35.46914534642596), 1019: (138.2782925992361, 35.738941455543326), 1020: (138.2782925992361, 35.873839510102), 1021: (138.42863286056377, 35.873839510102), 1022: (138.42863286056377, 35.738941455543326), 1023: (138.2782925992361, 36.00873756466068), 1024: (138.2782925992361, 36.14363561921936), 1025: (138.42863286056377, 36.14363561921936), 1026: (138.42863286056377, 36.00873756466068), 1027: (138.2782925992361, 36.27853367377804), 1028: (138.2782925992361, 36.41343172833672), 1029: (138.42863286056377, 36.41343172833672), 1030: (138.42863286056377, 36.27853367377804), 1031: (138.2782925992361, 36.548329782895394), 1032: (138.2782925992361, 36.683227837454076), 1033: (138.42863286056377, 36.683227837454076), 1034: (138.42863286056377, 36.548329782895394), 1035: (138.2782925992361, 36.81812589201276), 1036: (138.2782925992361, 36.953023946571435), 1037: (138.42863286056377, 36.953023946571435), 1038: (138.42863286056377, 36.81812589201276), 1039: (138.2782925992361, 37.08792200113011), 1040: (138.2782925992361, 37.22282005568879), 1041: (138.42863286056377, 37.22282005568879), 1042: (138.42863286056377, 37.08792200113011), 1043: (138.2782925992361, 37.357718110247475), 1044: (138.42863286056377, 37.357718110247475), 1045: (138.2782925992361, 37.89731032848219), 1046: (138.2782925992361, 38.03220838304087), 1047: (138.42863286056377, 38.03220838304087), 1048: (138.2782925992361, 38.16710643759954), 1049: (138.2782925992361, 38.302004492158225), 1050: (138.42863286056377, 38.302004492158225), 1051: (138.42863286056377, 38.16710643759954), 1052: (138.42863286056377, 38.43690254671691), 1053: (138.7293133832191, 34.79465507363257), 1054: (138.7293133832191, 34.65975701907389), 1055: (138.7293133832191, 35.06445118274993), 1056: (138.7293133832191, 34.929553128191245), 1057: (138.57897312189144, 35.19934923730861), 1058: (138.57897312189144, 35.334247291867285), 1059: (138.7293133832191, 35.334247291867285), 1060: (138.7293133832191, 35.19934923730861), 1061: (138.57897312189144, 35.46914534642596), 1062: (138.57897312189144, 35.604043400984644), 1063: (138.7293133832191, 35.604043400984644), 1064: (138.7293133832191, 35.46914534642596), 1065: (138.57897312189144, 35.738941455543326), 1066: (138.57897312189144, 35.873839510102), 1067: (138.7293133832191, 35.873839510102), 1068: (138.7293133832191, 35.738941455543326), 1069: (138.57897312189144, 36.00873756466068), 1070: (138.57897312189144, 36.14363561921936), 1071: (138.7293133832191, 36.14363561921936), 1072: (138.7293133832191, 36.00873756466068), 1073: (138.57897312189144, 36.27853367377804), 1074: (138.57897312189144, 36.41343172833672), 1075: (138.7293133832191, 36.41343172833672), 1076: (138.7293133832191, 36.27853367377804), 1077: (138.57897312189144, 36.548329782895394), 1078: (138.57897312189144, 36.683227837454076), 1079: (138.7293133832191, 36.683227837454076), 1080: (138.7293133832191, 36.548329782895394), 1081: (138.57897312189144, 36.81812589201276), 1082: (138.57897312189144, 36.953023946571435), 1083: (138.7293133832191, 36.953023946571435), 1084: (138.7293133832191, 36.81812589201276), 1085: (138.57897312189144, 37.08792200113011), 1086: (138.57897312189144, 37.22282005568879), 1087: (138.7293133832191, 37.22282005568879), 1088: (138.7293133832191, 37.08792200113011), 1089: (138.57897312189144, 37.357718110247475), 1090: (138.57897312189144, 37.49261616480615), 1091: (138.7293133832191, 37.49261616480615), 1092: (138.7293133832191, 37.357718110247475), 1093: (138.57897312189144, 37.627514219364826), 1094: (138.7293133832191, 37.76241227392351), 1095: (138.7293133832191, 37.627514219364826), 1096: (138.7293133832191, 37.89731032848219), 1097: (138.87965364454678, 34.79465507363257), 1098: (138.87965364454678, 34.929553128191245), 1099: (138.87965364454678, 35.06445118274993), 1100: (139.02999390587445, 35.06445118274993), 1101: (139.02999390587445, 34.929553128191245), 1102: (138.87965364454678, 35.19934923730861), 1103: (138.87965364454678, 35.334247291867285), 1104: (139.02999390587445, 35.334247291867285), 1105: (139.02999390587445, 35.19934923730861), 1106: (138.87965364454678, 35.46914534642596), 1107: (138.87965364454678, 35.604043400984644), 1108: (139.02999390587445, 35.604043400984644), 1109: (139.02999390587445, 35.46914534642596), 1110: (138.87965364454678, 35.738941455543326), 1111: (138.87965364454678, 35.873839510102), 1112: (139.02999390587445, 35.873839510102), 1113: (139.02999390587445, 35.738941455543326), 1114: (138.87965364454678, 36.00873756466068), 1115: (138.87965364454678, 36.14363561921936), 1116: (139.02999390587445, 36.14363561921936), 1117: (139.02999390587445, 36.00873756466068), 1118: (138.87965364454678, 36.27853367377804), 1119: (138.87965364454678, 36.41343172833672), 1120: (139.02999390587445, 36.41343172833672), 1121: (139.02999390587445, 36.27853367377804), 1122: (138.87965364454678, 36.548329782895394), 1123: (138.87965364454678, 36.683227837454076), 1124: (139.02999390587445, 36.683227837454076), 1125: (139.02999390587445, 36.548329782895394), 1126: (138.87965364454678, 36.81812589201276), 1127: (138.87965364454678, 36.953023946571435), 1128: (139.02999390587445, 36.953023946571435), 1129: (139.02999390587445, 36.81812589201276), 1130: (138.87965364454678, 37.08792200113011), 1131: (138.87965364454678, 37.22282005568879), 1132: (139.02999390587445, 37.22282005568879), 1133: (139.02999390587445, 37.08792200113011), 1134: (138.87965364454678, 37.357718110247475), 1135: (138.87965364454678, 37.49261616480615), 1136: (139.02999390587445, 37.49261616480615), 1137: (139.02999390587445, 37.357718110247475), 1138: (138.87965364454678, 37.627514219364826), 1139: (138.87965364454678, 37.76241227392351), 1140: (139.02999390587445, 37.76241227392351), 1141: (139.02999390587445, 37.627514219364826), 1142: (138.87965364454678, 37.89731032848219), 1143: (138.87965364454678, 38.03220838304087), 1144: (139.02999390587445, 38.03220838304087), 1145: (139.02999390587445, 37.89731032848219), 1146: (139.3306744285298, 34.79465507363257), 1147: (139.18033416720212, 35.46914534642596), 1148: (139.18033416720212, 35.604043400984644), 1149: (139.3306744285298, 35.604043400984644), 1150: (139.3306744285298, 35.46914534642596), 1151: (139.18033416720212, 35.738941455543326), 1152: (139.18033416720212, 35.873839510102), 1153: (139.3306744285298, 35.873839510102), 1154: (139.3306744285298, 35.738941455543326), 1155: (139.18033416720212, 36.00873756466068), 1156: (139.18033416720212, 36.14363561921936), 1157: (139.3306744285298, 36.14363561921936), 1158: (139.3306744285298, 36.00873756466068), 1159: (139.18033416720212, 36.27853367377804), 1160: (139.18033416720212, 36.41343172833672), 1161: (139.3306744285298, 36.41343172833672), 1162: (139.3306744285298, 36.27853367377804), 1163: (139.18033416720212, 36.548329782895394), 1164: (139.18033416720212, 36.683227837454076), 1165: (139.3306744285298, 36.683227837454076), 1166: (139.3306744285298, 36.548329782895394), 1167: (139.18033416720212, 36.81812589201276), 1168: (139.18033416720212, 36.953023946571435), 1169: (139.3306744285298, 36.953023946571435), 1170: (139.3306744285298, 36.81812589201276), 1171: (139.18033416720212, 37.08792200113011), 1172: (139.18033416720212, 37.22282005568879), 1173: (139.3306744285298, 37.22282005568879), 1174: (139.3306744285298, 37.08792200113011), 1175: (139.18033416720212, 37.357718110247475), 1176: (139.18033416720212, 37.49261616480615), 1177: (139.3306744285298, 37.49261616480615), 1178: (139.3306744285298, 37.357718110247475), 1179: (139.18033416720212, 37.627514219364826), 1180: (139.18033416720212, 37.76241227392351), 1181: (139.3306744285298, 37.76241227392351), 1182: (139.3306744285298, 37.627514219364826), 1183: (139.18033416720212, 37.89731032848219), 1184: (139.18033416720212, 38.03220838304087), 1185: (139.3306744285298, 38.03220838304087), 1186: (139.3306744285298, 37.89731032848219), 1187: (139.18033416720212, 38.16710643759954), 1188: (139.3306744285298, 38.302004492158225), 1189: (139.3306744285298, 38.16710643759954), 1190: (139.3306744285298, 38.43690254671691), 1191: (139.3306744285298, 42.21404807435992), 1192: (139.48101468985746, 35.334247291867285), 1193: (139.63135495118513, 35.334247291867285), 1194: (139.63135495118513, 35.19934923730861), 1195: (139.48101468985746, 35.46914534642596), 1196: (139.48101468985746, 35.604043400984644), 1197: (139.63135495118513, 35.604043400984644), 1198: (139.63135495118513, 35.46914534642596), 1199: (139.48101468985746, 35.738941455543326), 1200: (139.48101468985746, 35.873839510102), 1201: (139.63135495118513, 35.873839510102), 1202: (139.63135495118513, 35.738941455543326), 1203: (139.48101468985746, 36.00873756466068), 1204: (139.48101468985746, 36.14363561921936), 1205: (139.63135495118513, 36.14363561921936), 1206: (139.63135495118513, 36.00873756466068), 1207: (139.48101468985746, 36.27853367377804), 1208: (139.48101468985746, 36.41343172833672), 1209: (139.63135495118513, 36.41343172833672), 1210: (139.63135495118513, 36.27853367377804), 1211: (139.48101468985746, 36.548329782895394), 1212: (139.48101468985746, 36.683227837454076), 1213: (139.63135495118513, 36.683227837454076), 1214: (139.63135495118513, 36.548329782895394), 1215: (139.48101468985746, 36.81812589201276), 1216: (139.48101468985746, 36.953023946571435), 1217: (139.63135495118513, 36.953023946571435), 1218: (139.63135495118513, 36.81812589201276), 1219: (139.48101468985746, 37.08792200113011), 1220: (139.48101468985746, 37.22282005568879), 1221: (139.63135495118513, 37.22282005568879), 1222: (139.63135495118513, 37.08792200113011), 1223: (139.48101468985746, 37.357718110247475), 1224: (139.48101468985746, 37.49261616480615), 1225: (139.63135495118513, 37.49261616480615), 1226: (139.63135495118513, 37.357718110247475), 1227: (139.48101468985746, 37.627514219364826), 1228: (139.48101468985746, 37.76241227392351), 1229: (139.63135495118513, 37.76241227392351), 1230: (139.63135495118513, 37.627514219364826), 1231: (139.48101468985746, 37.89731032848219), 1232: (139.48101468985746, 38.03220838304087), 1233: (139.63135495118513, 38.03220838304087), 1234: (139.63135495118513, 37.89731032848219), 1235: (139.48101468985746, 38.16710643759954), 1236: (139.48101468985746, 38.302004492158225), 1237: (139.63135495118513, 38.302004492158225), 1238: (139.63135495118513, 38.16710643759954), 1239: (139.48101468985746, 38.43690254671691), 1240: (139.48101468985746, 38.571800601275584), 1241: (139.63135495118513, 38.571800601275584), 1242: (139.63135495118513, 38.43690254671691), 1243: (139.48101468985746, 38.70669865583426), 1244: (139.63135495118513, 38.84159671039294), 1245: (139.63135495118513, 38.70669865583426), 1246: (139.7816952125128, 34.929553128191245), 1247: (139.7816952125128, 35.06445118274993), 1248: (139.93203547384047, 35.06445118274993), 1249: (139.7816952125128, 35.19934923730861), 1250: (139.7816952125128, 35.334247291867285), 1251: (139.93203547384047, 35.334247291867285), 1252: (139.93203547384047, 35.19934923730861), 1253: (139.7816952125128, 35.46914534642596), 1254: (139.7816952125128, 35.604043400984644), 1255: (139.93203547384047, 35.604043400984644), 1256: (139.93203547384047, 35.46914534642596), 1257: (139.7816952125128, 35.738941455543326), 1258: (139.7816952125128, 35.873839510102), 1259: (139.93203547384047, 35.873839510102), 1260: (139.93203547384047, 35.738941455543326), 1261: (139.7816952125128, 36.00873756466068), 1262: (139.7816952125128, 36.14363561921936), 1263: (139.93203547384047, 36.14363561921936), 1264: (139.93203547384047, 36.00873756466068), 1265: (139.7816952125128, 36.27853367377804), 1266: (139.7816952125128, 36.41343172833672), 1267: (139.93203547384047, 36.41343172833672), 1268: (139.93203547384047, 36.27853367377804), 1269: (139.7816952125128, 36.548329782895394), 1270: (139.7816952125128, 36.683227837454076), 1271: (139.93203547384047, 36.683227837454076), 1272: (139.93203547384047, 36.548329782895394), 1273: (139.7816952125128, 36.81812589201276), 1274: (139.7816952125128, 36.953023946571435), 1275: (139.93203547384047, 36.953023946571435), 1276: (139.93203547384047, 36.81812589201276), 1277: (139.7816952125128, 37.08792200113011), 1278: (139.7816952125128, 37.22282005568879), 1279: (139.93203547384047, 37.22282005568879), 1280: (139.93203547384047, 37.08792200113011), 1281: (139.7816952125128, 37.357718110247475), 1282: (139.7816952125128, 37.49261616480615), 1283: (139.93203547384047, 37.49261616480615), 1284: (139.93203547384047, 37.357718110247475), 1285: (139.7816952125128, 37.627514219364826), 1286: (139.7816952125128, 37.76241227392351), 1287: (139.93203547384047, 37.76241227392351), 1288: (139.93203547384047, 37.627514219364826), 1289: (139.7816952125128, 37.89731032848219), 1290: (139.7816952125128, 38.03220838304087), 1291: (139.93203547384047, 38.03220838304087), 1292: (139.93203547384047, 37.89731032848219), 1293: (139.7816952125128, 38.16710643759954), 1294: (139.7816952125128, 38.302004492158225), 1295: (139.93203547384047, 38.302004492158225), 1296: (139.93203547384047, 38.16710643759954), 1297: (139.7816952125128, 38.43690254671691), 1298: (139.7816952125128, 38.571800601275584), 1299: (139.93203547384047, 38.571800601275584), 1300: (139.93203547384047, 38.43690254671691), 1301: (139.7816952125128, 38.70669865583426), 1302: (139.7816952125128, 38.84159671039294), 1303: (139.93203547384047, 38.84159671039294), 1304: (139.93203547384047, 38.70669865583426), 1305: (139.7816952125128, 38.976494764951624), 1306: (139.7816952125128, 39.1113928195103), 1307: (139.93203547384047, 39.1113928195103), 1308: (139.93203547384047, 38.976494764951624), 1309: (139.7816952125128, 39.246290874068976), 1310: (139.93203547384047, 39.38118892862766), 1311: (139.93203547384047, 39.246290874068976), 1312: (139.7816952125128, 39.920781146862375), 1313: (139.93203547384047, 39.920781146862375), 1314: (139.93203547384047, 39.78588309230369), 1315: (139.7816952125128, 40.05567920142106), 1316: (139.93203547384047, 40.19057725597973), 1317: (139.93203547384047, 40.05567920142106), 1318: (139.7816952125128, 40.73016947421445), 1319: (139.93203547384047, 40.73016947421445), 1320: (139.93203547384047, 40.595271419655774), 1321: (139.93203547384047, 41.539557801566524), 1322: (139.93203547384047, 41.80935391068388), 1323: (139.93203547384047, 41.674455856125206), 1324: (139.7816952125128, 42.21404807435992), 1325: (139.7816952125128, 42.3489461289186), 1326: (139.93203547384047, 42.3489461289186), 1327: (139.93203547384047, 42.21404807435992), 1328: (139.7816952125128, 42.483844183477274), 1329: (139.7816952125128, 42.618742238035956), 1330: (139.93203547384047, 42.618742238035956), 1331: (139.93203547384047, 42.483844183477274), 1332: (139.7816952125128, 42.75364029259464), 1333: (139.93203547384047, 42.75364029259464), 1334: (140.08237573516814, 35.19934923730861), 1335: (140.08237573516814, 35.334247291867285), 1336: (140.2327159964958, 35.334247291867285), 1337: (140.2327159964958, 35.19934923730861), 1338: (140.08237573516814, 35.46914534642596), 1339: (140.08237573516814, 35.604043400984644), 1340: (140.2327159964958, 35.604043400984644), 1341: (140.2327159964958, 35.46914534642596), 1342: (140.08237573516814, 35.738941455543326), 1343: (140.08237573516814, 35.873839510102), 1344: (140.2327159964958, 35.873839510102), 1345: (140.2327159964958, 35.738941455543326), 1346: (140.08237573516814, 36.00873756466068), 1347: (140.08237573516814, 36.14363561921936), 1348: (140.2327159964958, 36.14363561921936), 1349: (140.2327159964958, 36.00873756466068), 1350: (140.08237573516814, 36.27853367377804), 1351: (140.08237573516814, 36.41343172833672), 1352: (140.2327159964958, 36.41343172833672), 1353: (140.2327159964958, 36.27853367377804), 1354: (140.08237573516814, 36.548329782895394), 1355: (140.08237573516814, 36.683227837454076), 1356: (140.2327159964958, 36.683227837454076), 1357: (140.2327159964958, 36.548329782895394), 1358: (140.08237573516814, 36.81812589201276), 1359: (140.08237573516814, 36.953023946571435), 1360: (140.2327159964958, 36.953023946571435), 1361: (140.2327159964958, 36.81812589201276), 1362: (140.08237573516814, 37.08792200113011), 1363: (140.08237573516814, 37.22282005568879), 1364: (140.2327159964958, 37.22282005568879), 1365: (140.2327159964958, 37.08792200113011), 1366: (140.08237573516814, 37.357718110247475), 1367: (140.08237573516814, 37.49261616480615), 1368: (140.2327159964958, 37.49261616480615), 1369: (140.2327159964958, 37.357718110247475), 1370: (140.08237573516814, 37.627514219364826), 1371: (140.08237573516814, 37.76241227392351), 1372: (140.2327159964958, 37.76241227392351), 1373: (140.2327159964958, 37.627514219364826), 1374: (140.08237573516814, 37.89731032848219), 1375: (140.08237573516814, 38.03220838304087), 1376: (140.2327159964958, 38.03220838304087), 1377: (140.2327159964958, 37.89731032848219), 1378: (140.08237573516814, 38.16710643759954), 1379: (140.08237573516814, 38.302004492158225), 1380: (140.2327159964958, 38.302004492158225), 1381: (140.2327159964958, 38.16710643759954), 1382: (140.08237573516814, 38.43690254671691), 1383: (140.08237573516814, 38.571800601275584), 1384: (140.2327159964958, 38.571800601275584), 1385: (140.2327159964958, 38.43690254671691), 1386: (140.08237573516814, 38.70669865583426), 1387: (140.08237573516814, 38.84159671039294), 1388: (140.2327159964958, 38.84159671039294), 1389: (140.2327159964958, 38.70669865583426), 1390: (140.08237573516814, 38.976494764951624), 1391: (140.08237573516814, 39.1113928195103), 1392: (140.2327159964958, 39.1113928195103), 1393: (140.2327159964958, 38.976494764951624), 1394: (140.08237573516814, 39.246290874068976), 1395: (140.08237573516814, 39.38118892862766), 1396: (140.2327159964958, 39.38118892862766), 1397: (140.2327159964958, 39.246290874068976), 1398: (140.08237573516814, 39.51608698318634), 1399: (140.08237573516814, 39.650985037745016), 1400: (140.2327159964958, 39.650985037745016), 1401: (140.2327159964958, 39.51608698318634), 1402: (140.08237573516814, 39.78588309230369), 1403: (140.08237573516814, 39.920781146862375), 1404: (140.2327159964958, 39.920781146862375), 1405: (140.2327159964958, 39.78588309230369), 1406: (140.08237573516814, 40.05567920142106), 1407: (140.08237573516814, 40.19057725597973), 1408: (140.2327159964958, 40.19057725597973), 1409: (140.2327159964958, 40.05567920142106), 1410: (140.08237573516814, 40.32547531053841), 1411: (140.08237573516814, 40.46037336509709), 1412: (140.2327159964958, 40.46037336509709), 1413: (140.2327159964958, 40.32547531053841), 1414: (140.08237573516814, 40.595271419655774), 1415: (140.08237573516814, 40.73016947421445), 1416: (140.2327159964958, 40.73016947421445), 1417: (140.2327159964958, 40.595271419655774), 1418: (140.08237573516814, 40.865067528773125), 1419: (140.2327159964958, 40.99996558333181), 1420: (140.2327159964958, 40.865067528773125), 1421: (140.2327159964958, 41.269761692449165), 1422: (140.2327159964958, 41.13486363789049), 1423: (140.08237573516814, 41.539557801566524), 1424: (140.2327159964958, 41.539557801566524), 1425: (140.08237573516814, 41.674455856125206), 1426: (140.08237573516814, 41.80935391068388), 1427: (140.2327159964958, 41.80935391068388), 1428: (140.2327159964958, 41.674455856125206), 1429: (140.08237573516814, 41.94425196524256), 1430: (140.08237573516814, 42.07915001980124), 1431: (140.2327159964958, 42.07915001980124), 1432: (140.2327159964958, 41.94425196524256), 1433: (140.08237573516814, 42.21404807435992), 1434: (140.08237573516814, 42.3489461289186), 1435: (140.2327159964958, 42.3489461289186), 1436: (140.2327159964958, 42.21404807435992), 1437: (140.08237573516814, 42.483844183477274), 1438: (140.08237573516814, 42.618742238035956), 1439: (140.2327159964958, 42.618742238035956), 1440: (140.2327159964958, 42.483844183477274), 1441: (140.08237573516814, 42.75364029259464), 1442: (140.08237573516814, 42.888538347153315), 1443: (140.2327159964958, 42.888538347153315), 1444: (140.2327159964958, 42.75364029259464), 1445: (140.38305625782348, 35.604043400984644), 1446: (140.38305625782348, 35.738941455543326), 1447: (140.38305625782348, 35.873839510102), 1448: (140.53339651915115, 35.873839510102), 1449: (140.53339651915115, 35.738941455543326), 1450: (140.38305625782348, 36.00873756466068), 1451: (140.38305625782348, 36.14363561921936), 1452: (140.53339651915115, 36.14363561921936), 1453: (140.53339651915115, 36.00873756466068), 1454: (140.38305625782348, 36.27853367377804), 1455: (140.38305625782348, 36.41343172833672), 1456: (140.53339651915115, 36.41343172833672), 1457: (140.53339651915115, 36.27853367377804), 1458: (140.38305625782348, 36.548329782895394), 1459: (140.38305625782348, 36.683227837454076), 1460: (140.53339651915115, 36.683227837454076), 1461: (140.53339651915115, 36.548329782895394), 1462: (140.38305625782348, 36.81812589201276), 1463: (140.38305625782348, 36.953023946571435), 1464: (140.53339651915115, 36.953023946571435), 1465: (140.53339651915115, 36.81812589201276), 1466: (140.38305625782348, 37.08792200113011), 1467: (140.38305625782348, 37.22282005568879), 1468: (140.53339651915115, 37.22282005568879), 1469: (140.53339651915115, 37.08792200113011), 1470: (140.38305625782348, 37.357718110247475), 1471: (140.38305625782348, 37.49261616480615), 1472: (140.53339651915115, 37.49261616480615), 1473: (140.53339651915115, 37.357718110247475), 1474: (140.38305625782348, 37.627514219364826), 1475: (140.38305625782348, 37.76241227392351), 1476: (140.53339651915115, 37.76241227392351), 1477: (140.53339651915115, 37.627514219364826), 1478: (140.38305625782348, 37.89731032848219), 1479: (140.38305625782348, 38.03220838304087), 1480: (140.53339651915115, 38.03220838304087), 1481: (140.53339651915115, 37.89731032848219), 1482: (140.38305625782348, 38.16710643759954), 1483: (140.38305625782348, 38.302004492158225), 1484: (140.53339651915115, 38.302004492158225), 1485: (140.53339651915115, 38.16710643759954), 1486: (140.38305625782348, 38.43690254671691), 1487: (140.38305625782348, 38.571800601275584), 1488: (140.53339651915115, 38.571800601275584), 1489: (140.53339651915115, 38.43690254671691), 1490: (140.38305625782348, 38.70669865583426), 1491: (140.38305625782348, 38.84159671039294), 1492: (140.53339651915115, 38.84159671039294), 1493: (140.53339651915115, 38.70669865583426), 1494: (140.38305625782348, 38.976494764951624), 1495: (140.38305625782348, 39.1113928195103), 1496: (140.53339651915115, 39.1113928195103), 1497: (140.53339651915115, 38.976494764951624), 1498: (140.38305625782348, 39.246290874068976), 1499: (140.38305625782348, 39.38118892862766), 1500: (140.53339651915115, 39.38118892862766), 1501: (140.53339651915115, 39.246290874068976), 1502: (140.38305625782348, 39.51608698318634), 1503: (140.38305625782348, 39.650985037745016), 1504: (140.53339651915115, 39.650985037745016), 1505: (140.53339651915115, 39.51608698318634), 1506: (140.38305625782348, 39.78588309230369), 1507: (140.38305625782348, 39.920781146862375), 1508: (140.53339651915115, 39.920781146862375), 1509: (140.53339651915115, 39.78588309230369), 1510: (140.38305625782348, 40.05567920142106), 1511: (140.38305625782348, 40.19057725597973), 1512: (140.53339651915115, 40.19057725597973), 1513: (140.53339651915115, 40.05567920142106), 1514: (140.38305625782348, 40.32547531053841), 1515: (140.38305625782348, 40.46037336509709), 1516: (140.53339651915115, 40.46037336509709), 1517: (140.53339651915115, 40.32547531053841), 1518: (140.38305625782348, 40.595271419655774), 1519: (140.38305625782348, 40.73016947421445), 1520: (140.53339651915115, 40.73016947421445), 1521: (140.53339651915115, 40.595271419655774), 1522: (140.38305625782348, 40.865067528773125), 1523: (140.38305625782348, 40.99996558333181), 1524: (140.53339651915115, 40.99996558333181), 1525: (140.53339651915115, 40.865067528773125), 1526: (140.38305625782348, 41.13486363789049), 1527: (140.38305625782348, 41.269761692449165), 1528: (140.53339651915115, 41.269761692449165), 1529: (140.53339651915115, 41.13486363789049), 1530: (140.38305625782348, 41.674455856125206), 1531: (140.38305625782348, 41.80935391068388), 1532: (140.53339651915115, 41.80935391068388), 1533: (140.38305625782348, 41.94425196524256), 1534: (140.38305625782348, 42.07915001980124), 1535: (140.53339651915115, 42.07915001980124), 1536: (140.53339651915115, 41.94425196524256), 1537: (140.38305625782348, 42.21404807435992), 1538: (140.53339651915115, 42.21404807435992), 1539: (140.38305625782348, 42.618742238035956), 1540: (140.53339651915115, 42.618742238035956), 1541: (140.38305625782348, 42.75364029259464), 1542: (140.38305625782348, 42.888538347153315), 1543: (140.53339651915115, 42.888538347153315), 1544: (140.53339651915115, 42.75364029259464), 1545: (140.38305625782348, 43.02343640171199), 1546: (140.38305625782348, 43.15833445627067), 1547: (140.53339651915115, 43.15833445627067), 1548: (140.53339651915115, 43.02343640171199), 1549: (140.38305625782348, 43.293232510829355), 1550: (140.38305625782348, 43.42813056538803), 1551: (140.53339651915115, 43.293232510829355), 1552: (140.68373678047882, 35.738941455543326), 1553: (140.68373678047882, 35.873839510102), 1554: (140.68373678047882, 36.81812589201276), 1555: (140.68373678047882, 36.953023946571435), 1556: (140.8340770418065, 36.953023946571435), 1557: (140.68373678047882, 37.08792200113011), 1558: (140.68373678047882, 37.22282005568879), 1559: (140.8340770418065, 37.22282005568879), 1560: (140.8340770418065, 37.08792200113011), 1561: (140.68373678047882, 37.357718110247475), 1562: (140.68373678047882, 37.49261616480615), 1563: (140.8340770418065, 37.49261616480615), 1564: (140.8340770418065, 37.357718110247475), 1565: (140.68373678047882, 37.627514219364826), 1566: (140.68373678047882, 37.76241227392351), 1567: (140.8340770418065, 37.76241227392351), 1568: (140.8340770418065, 37.627514219364826), 1569: (140.68373678047882, 37.89731032848219), 1570: (140.68373678047882, 38.03220838304087), 1571: (140.8340770418065, 38.03220838304087), 1572: (140.8340770418065, 37.89731032848219), 1573: (140.68373678047882, 38.16710643759954), 1574: (140.68373678047882, 38.302004492158225), 1575: (140.8340770418065, 38.302004492158225), 1576: (140.8340770418065, 38.16710643759954), 1577: (140.68373678047882, 38.43690254671691), 1578: (140.68373678047882, 38.571800601275584), 1579: (140.8340770418065, 38.571800601275584), 1580: (140.8340770418065, 38.43690254671691), 1581: (140.68373678047882, 38.70669865583426), 1582: (140.68373678047882, 38.84159671039294), 1583: (140.8340770418065, 38.84159671039294), 1584: (140.8340770418065, 38.70669865583426), 1585: (140.68373678047882, 38.976494764951624), 1586: (140.68373678047882, 39.1113928195103), 1587: (140.8340770418065, 39.1113928195103), 1588: (140.8340770418065, 38.976494764951624), 1589: (140.68373678047882, 39.246290874068976), 1590: (140.68373678047882, 39.38118892862766), 1591: (140.8340770418065, 39.38118892862766), 1592: (140.8340770418065, 39.246290874068976), 1593: (140.68373678047882, 39.51608698318634), 1594: (140.68373678047882, 39.650985037745016), 1595: (140.8340770418065, 39.650985037745016), 1596: (140.8340770418065, 39.51608698318634), 1597: (140.68373678047882, 39.78588309230369), 1598: (140.68373678047882, 39.920781146862375), 1599: (140.8340770418065, 39.920781146862375), 1600: (140.8340770418065, 39.78588309230369), 1601: (140.68373678047882, 40.05567920142106), 1602: (140.68373678047882, 40.19057725597973), 1603: (140.8340770418065, 40.19057725597973), 1604: (140.8340770418065, 40.05567920142106), 1605: (140.68373678047882, 40.32547531053841), 1606: (140.68373678047882, 40.46037336509709), 1607: (140.8340770418065, 40.46037336509709), 1608: (140.8340770418065, 40.32547531053841), 1609: (140.68373678047882, 40.595271419655774), 1610: (140.68373678047882, 40.73016947421445), 1611: (140.8340770418065, 40.73016947421445), 1612: (140.8340770418065, 40.595271419655774), 1613: (140.68373678047882, 40.865067528773125), 1614: (140.68373678047882, 40.99996558333181), 1615: (140.8340770418065, 40.99996558333181), 1616: (140.8340770418065, 40.865067528773125), 1617: (140.68373678047882, 41.269761692449165), 1618: (140.8340770418065, 41.269761692449165), 1619: (140.68373678047882, 41.40465974700784), 1620: (140.68373678047882, 41.539557801566524), 1621: (140.8340770418065, 41.539557801566524), 1622: (140.8340770418065, 41.40465974700784), 1623: (140.68373678047882, 41.80935391068388), 1624: (140.8340770418065, 41.80935391068388), 1625: (140.68373678047882, 41.94425196524256), 1626: (140.68373678047882, 42.07915001980124), 1627: (140.8340770418065, 42.07915001980124), 1628: (140.8340770418065, 41.94425196524256), 1629: (140.68373678047882, 42.21404807435992), 1630: (140.68373678047882, 42.618742238035956), 1631: (140.8340770418065, 42.618742238035956), 1632: (140.8340770418065, 42.483844183477274), 1633: (140.68373678047882, 42.75364029259464), 1634: (140.68373678047882, 42.888538347153315), 1635: (140.8340770418065, 42.888538347153315), 1636: (140.8340770418065, 42.75364029259464), 1637: (140.68373678047882, 43.02343640171199), 1638: (140.68373678047882, 43.15833445627067), 1639: (140.8340770418065, 43.15833445627067), 1640: (140.8340770418065, 43.02343640171199), 1641: (140.68373678047882, 43.293232510829355), 1642: (140.8340770418065, 43.293232510829355), 1643: (140.98441730313417, 37.357718110247475), 1644: (140.98441730313417, 37.49261616480615), 1645: (140.98441730313417, 37.627514219364826), 1646: (140.98441730313417, 37.76241227392351), 1647: (140.98441730313417, 38.43690254671691), 1648: (140.98441730313417, 38.571800601275584), 1649: (141.13475756446184, 38.571800601275584), 1650: (141.13475756446184, 38.43690254671691), 1651: (140.98441730313417, 38.70669865583426), 1652: (140.98441730313417, 38.84159671039294), 1653: (141.13475756446184, 38.84159671039294), 1654: (141.13475756446184, 38.70669865583426), 1655: (140.98441730313417, 38.976494764951624), 1656: (140.98441730313417, 39.1113928195103), 1657: (141.13475756446184, 39.1113928195103), 1658: (141.13475756446184, 38.976494764951624), 1659: (140.98441730313417, 39.246290874068976), 1660: (140.98441730313417, 39.38118892862766), 1661: (141.13475756446184, 39.38118892862766), 1662: (141.13475756446184, 39.246290874068976), 1663: (140.98441730313417, 39.51608698318634), 1664: (140.98441730313417, 39.650985037745016), 1665: (141.13475756446184, 39.650985037745016), 1666: (141.13475756446184, 39.51608698318634), 1667: (140.98441730313417, 39.78588309230369), 1668: (140.98441730313417, 39.920781146862375), 1669: (141.13475756446184, 39.920781146862375), 1670: (141.13475756446184, 39.78588309230369), 1671: (140.98441730313417, 40.05567920142106), 1672: (140.98441730313417, 40.19057725597973), 1673: (141.13475756446184, 40.19057725597973), 1674: (141.13475756446184, 40.05567920142106), 1675: (140.98441730313417, 40.32547531053841), 1676: (140.98441730313417, 40.46037336509709), 1677: (141.13475756446184, 40.46037336509709), 1678: (141.13475756446184, 40.32547531053841), 1679: (140.98441730313417, 40.595271419655774), 1680: (140.98441730313417, 40.73016947421445), 1681: (141.13475756446184, 40.73016947421445), 1682: (141.13475756446184, 40.595271419655774), 1683: (140.98441730313417, 40.865067528773125), 1684: (140.98441730313417, 40.99996558333181), 1685: (141.13475756446184, 40.99996558333181), 1686: (141.13475756446184, 40.865067528773125), 1687: (140.98441730313417, 41.269761692449165), 1688: (141.13475756446184, 41.269761692449165), 1689: (141.13475756446184, 41.13486363789049), 1690: (140.98441730313417, 41.40465974700784), 1691: (140.98441730313417, 41.539557801566524), 1692: (141.13475756446184, 41.40465974700784), 1693: (140.98441730313417, 41.80935391068388), 1694: (140.98441730313417, 41.94425196524256), 1695: (140.98441730313417, 42.483844183477274), 1696: (140.98441730313417, 42.618742238035956), 1697: (141.13475756446184, 42.618742238035956), 1698: (141.13475756446184, 42.483844183477274), 1699: (140.98441730313417, 42.75364029259464), 1700: (140.98441730313417, 42.888538347153315), 1701: (141.13475756446184, 42.888538347153315), 1702: (141.13475756446184, 42.75364029259464), 1703: (140.98441730313417, 43.02343640171199), 1704: (140.98441730313417, 43.15833445627067), 1705: (141.13475756446184, 43.15833445627067), 1706: (141.13475756446184, 43.02343640171199), 1707: (140.98441730313417, 45.31670332920954), 1708: (141.13475756446184, 45.31670332920954), 1709: (141.13475756446184, 45.181805274650856), 1710: (140.98441730313417, 45.45160138376822), 1711: (141.2850978257895, 38.43690254671691), 1712: (141.2850978257895, 38.571800601275584), 1713: (141.43543808711718, 38.571800601275584), 1714: (141.43543808711718, 38.43690254671691), 1715: (141.2850978257895, 38.70669865583426), 1716: (141.2850978257895, 38.84159671039294), 1717: (141.43543808711718, 38.84159671039294), 1718: (141.43543808711718, 38.70669865583426), 1719: (141.2850978257895, 38.976494764951624), 1720: (141.2850978257895, 39.1113928195103), 1721: (141.43543808711718, 39.1113928195103), 1722: (141.43543808711718, 38.976494764951624), 1723: (141.2850978257895, 39.246290874068976), 1724: (141.2850978257895, 39.38118892862766), 1725: (141.43543808711718, 39.38118892862766), 1726: (141.43543808711718, 39.246290874068976), 1727: (141.2850978257895, 39.51608698318634), 1728: (141.2850978257895, 39.650985037745016), 1729: (141.43543808711718, 39.650985037745016), 1730: (141.43543808711718, 39.51608698318634), 1731: (141.2850978257895, 39.78588309230369), 1732: (141.2850978257895, 39.920781146862375), 1733: (141.43543808711718, 39.920781146862375), 1734: (141.43543808711718, 39.78588309230369), 1735: (141.2850978257895, 40.05567920142106), 1736: (141.2850978257895, 40.19057725597973), 1737: (141.43543808711718, 40.19057725597973), 1738: (141.43543808711718, 40.05567920142106), 1739: (141.2850978257895, 40.32547531053841), 1740: (141.2850978257895, 40.46037336509709), 1741: (141.43543808711718, 40.46037336509709), 1742: (141.43543808711718, 40.32547531053841), 1743: (141.2850978257895, 40.595271419655774), 1744: (141.2850978257895, 40.73016947421445), 1745: (141.43543808711718, 40.595271419655774), 1746: (141.2850978257895, 40.865067528773125), 1747: (141.2850978257895, 40.99996558333181), 1748: (141.2850978257895, 41.13486363789049), 1749: (141.2850978257895, 41.269761692449165), 1750: (141.2850978257895, 41.40465974700784), 1751: (141.2850978257895, 42.618742238035956), 1752: (141.43543808711718, 42.618742238035956), 1753: (141.2850978257895, 42.75364029259464), 1754: (141.2850978257895, 42.888538347153315), 1755: (141.43543808711718, 42.888538347153315), 1756: (141.43543808711718, 42.75364029259464), 1757: (141.2850978257895, 43.02343640171199), 1758: (141.2850978257895, 43.15833445627067), 1759: (141.43543808711718, 43.15833445627067), 1760: (141.43543808711718, 43.02343640171199), 1761: (141.2850978257895, 43.293232510829355), 1762: (141.43543808711718, 43.42813056538803), 1763: (141.43543808711718, 43.293232510829355), 1764: (141.2850978257895, 43.56302861994671), 1765: (141.2850978257895, 43.69792667450539), 1766: (141.43543808711718, 43.69792667450539), 1767: (141.43543808711718, 43.56302861994671), 1768: (141.2850978257895, 43.83282472906407), 1769: (141.43543808711718, 43.96772278362275), 1770: (141.43543808711718, 43.83282472906407), 1771: (141.58577834844485, 38.976494764951624), 1772: (141.58577834844485, 39.1113928195103), 1773: (141.73611860977252, 39.1113928195103), 1774: (141.58577834844485, 39.246290874068976), 1775: (141.58577834844485, 39.38118892862766), 1776: (141.73611860977252, 39.38118892862766), 1777: (141.73611860977252, 39.246290874068976), 1778: (141.58577834844485, 39.51608698318634), 1779: (141.58577834844485, 39.650985037745016), 1780: (141.73611860977252, 39.650985037745016), 1781: (141.73611860977252, 39.51608698318634), 1782: (141.58577834844485, 39.78588309230369), 1783: (141.58577834844485, 39.920781146862375), 1784: (141.73611860977252, 39.920781146862375), 1785: (141.73611860977252, 39.78588309230369), 1786: (141.58577834844485, 40.05567920142106), 1787: (141.58577834844485, 40.19057725597973), 1788: (141.73611860977252, 40.19057725597973), 1789: (141.73611860977252, 40.05567920142106), 1790: (141.58577834844485, 40.32547531053841), 1791: (141.58577834844485, 40.46037336509709), 1792: (141.73611860977252, 40.32547531053841), 1793: (141.58577834844485, 42.75364029259464), 1794: (141.58577834844485, 42.888538347153315), 1795: (141.73611860977252, 42.888538347153315), 1796: (141.73611860977252, 42.75364029259464), 1797: (141.58577834844485, 43.02343640171199), 1798: (141.58577834844485, 43.15833445627067), 1799: (141.73611860977252, 43.15833445627067), 1800: (141.73611860977252, 43.02343640171199), 1801: (141.58577834844485, 43.293232510829355), 1802: (141.58577834844485, 43.42813056538803), 1803: (141.73611860977252, 43.42813056538803), 1804: (141.73611860977252, 43.293232510829355), 1805: (141.58577834844485, 43.56302861994671), 1806: (141.58577834844485, 43.69792667450539), 1807: (141.73611860977252, 43.69792667450539), 1808: (141.73611860977252, 43.56302861994671), 1809: (141.58577834844485, 43.83282472906407), 1810: (141.58577834844485, 43.96772278362275), 1811: (141.73611860977252, 43.96772278362275), 1812: (141.73611860977252, 43.83282472906407), 1813: (141.58577834844485, 44.10262083818142), 1814: (141.58577834844485, 44.237518892740106), 1815: (141.73611860977252, 44.237518892740106), 1816: (141.73611860977252, 44.10262083818142), 1817: (141.58577834844485, 44.37241694729879), 1818: (141.73611860977252, 44.507315001857464), 1819: (141.73611860977252, 44.37241694729879), 1820: (141.73611860977252, 44.77711111097482), 1821: (141.73611860977252, 44.64221305641614), 1822: (141.58577834844485, 45.04690722009218), 1823: (141.73611860977252, 45.04690722009218), 1824: (141.73611860977252, 44.912009165533505), 1825: (141.58577834844485, 45.181805274650856), 1826: (141.58577834844485, 45.31670332920954), 1827: (141.73611860977252, 45.31670332920954), 1828: (141.73611860977252, 45.181805274650856), 1829: (141.58577834844485, 45.45160138376822), 1830: (141.73611860977252, 45.586499438326896), 1831: (141.73611860977252, 45.45160138376822), 1832: (141.8864588711002, 39.246290874068976), 1833: (141.8864588711002, 39.38118892862766), 1834: (141.8864588711002, 39.51608698318634), 1835: (141.8864588711002, 39.650985037745016), 1836: (141.8864588711002, 39.78588309230369), 1837: (141.8864588711002, 39.920781146862375), 1838: (141.8864588711002, 40.05567920142106), 1839: (141.8864588711002, 42.618742238035956), 1840: (142.03679913242786, 42.618742238035956), 1841: (141.8864588711002, 42.75364029259464), 1842: (141.8864588711002, 42.888538347153315), 1843: (142.03679913242786, 42.888538347153315), 1844: (142.03679913242786, 42.75364029259464), 1845: (141.8864588711002, 43.02343640171199), 1846: (141.8864588711002, 43.15833445627067), 1847: (142.03679913242786, 43.15833445627067), 1848: (142.03679913242786, 43.02343640171199), 1849: (141.8864588711002, 43.293232510829355), 1850: (141.8864588711002, 43.42813056538803), 1851: (142.03679913242786, 43.42813056538803), 1852: (142.03679913242786, 43.293232510829355), 1853: (141.8864588711002, 43.56302861994671), 1854: (141.8864588711002, 43.69792667450539), 1855: (142.03679913242786, 43.69792667450539), 1856: (142.03679913242786, 43.56302861994671), 1857: (141.8864588711002, 43.83282472906407), 1858: (141.8864588711002, 43.96772278362275), 1859: (142.03679913242786, 43.96772278362275), 1860: (142.03679913242786, 43.83282472906407), 1861: (141.8864588711002, 44.10262083818142), 1862: (141.8864588711002, 44.237518892740106), 1863: (142.03679913242786, 44.237518892740106), 1864: (142.03679913242786, 44.10262083818142), 1865: (141.8864588711002, 44.37241694729879), 1866: (141.8864588711002, 44.507315001857464), 1867: (142.03679913242786, 44.507315001857464), 1868: (142.03679913242786, 44.37241694729879), 1869: (141.8864588711002, 44.64221305641614), 1870: (141.8864588711002, 44.77711111097482), 1871: (142.03679913242786, 44.77711111097482), 1872: (142.03679913242786, 44.64221305641614), 1873: (141.8864588711002, 44.912009165533505), 1874: (141.8864588711002, 45.04690722009218), 1875: (142.03679913242786, 45.04690722009218), 1876: (142.03679913242786, 44.912009165533505), 1877: (141.8864588711002, 45.181805274650856), 1878: (141.8864588711002, 45.31670332920954), 1879: (142.03679913242786, 45.31670332920954), 1880: (142.03679913242786, 45.181805274650856), 1881: (141.8864588711002, 45.45160138376822), 1882: (141.8864588711002, 45.586499438326896), 1883: (142.03679913242786, 45.45160138376822), 1884: (142.18713939375553, 42.483844183477274), 1885: (142.18713939375553, 42.618742238035956), 1886: (142.3374796550832, 42.618742238035956), 1887: (142.3374796550832, 42.483844183477274), 1888: (142.18713939375553, 42.75364029259464), 1889: (142.18713939375553, 42.888538347153315), 1890: (142.3374796550832, 42.888538347153315), 1891: (142.3374796550832, 42.75364029259464), 1892: (142.18713939375553, 43.02343640171199), 1893: (142.18713939375553, 43.15833445627067), 1894: (142.3374796550832, 43.15833445627067), 1895: (142.3374796550832, 43.02343640171199), 1896: (142.18713939375553, 43.293232510829355), 1897: (142.18713939375553, 43.42813056538803), 1898: (142.3374796550832, 43.42813056538803), 1899: (142.3374796550832, 43.293232510829355), 1900: (142.18713939375553, 43.56302861994671), 1901: (142.18713939375553, 43.69792667450539), 1902: (142.3374796550832, 43.69792667450539), 1903: (142.3374796550832, 43.56302861994671), 1904: (142.18713939375553, 43.83282472906407), 1905: (142.18713939375553, 43.96772278362275), 1906: (142.3374796550832, 43.96772278362275), 1907: (142.3374796550832, 43.83282472906407), 1908: (142.18713939375553, 44.10262083818142), 1909: (142.18713939375553, 44.237518892740106), 1910: (142.3374796550832, 44.237518892740106), 1911: (142.3374796550832, 44.10262083818142), 1912: (142.18713939375553, 44.37241694729879), 1913: (142.18713939375553, 44.507315001857464), 1914: (142.3374796550832, 44.507315001857464), 1915: (142.3374796550832, 44.37241694729879), 1916: (142.18713939375553, 44.64221305641614), 1917: (142.18713939375553, 44.77711111097482), 1918: (142.3374796550832, 44.77711111097482), 1919: (142.3374796550832, 44.64221305641614), 1920: (142.18713939375553, 44.912009165533505), 1921: (142.18713939375553, 45.04690722009218), 1922: (142.3374796550832, 45.04690722009218), 1923: (142.3374796550832, 44.912009165533505), 1924: (142.18713939375553, 45.181805274650856), 1925: (142.18713939375553, 45.31670332920954), 1926: (142.3374796550832, 45.181805274650856), 1927: (142.48781991641087, 42.3489461289186), 1928: (142.63816017773854, 42.3489461289186), 1929: (142.63816017773854, 42.21404807435992), 1930: (142.48781991641087, 42.483844183477274), 1931: (142.48781991641087, 42.618742238035956), 1932: (142.63816017773854, 42.618742238035956), 1933: (142.63816017773854, 42.483844183477274), 1934: (142.48781991641087, 42.75364029259464), 1935: (142.48781991641087, 42.888538347153315), 1936: (142.63816017773854, 42.888538347153315), 1937: (142.63816017773854, 42.75364029259464), 1938: (142.48781991641087, 43.02343640171199), 1939: (142.48781991641087, 43.15833445627067), 1940: (142.63816017773854, 43.15833445627067), 1941: (142.63816017773854, 43.02343640171199), 1942: (142.48781991641087, 43.293232510829355), 1943: (142.48781991641087, 43.42813056538803), 1944: (142.63816017773854, 43.42813056538803), 1945: (142.63816017773854, 43.293232510829355), 1946: (142.48781991641087, 43.56302861994671), 1947: (142.48781991641087, 43.69792667450539), 1948: (142.63816017773854, 43.69792667450539), 1949: (142.63816017773854, 43.56302861994671), 1950: (142.48781991641087, 43.83282472906407), 1951: (142.48781991641087, 43.96772278362275), 1952: (142.63816017773854, 43.96772278362275), 1953: (142.63816017773854, 43.83282472906407), 1954: (142.48781991641087, 44.10262083818142), 1955: (142.48781991641087, 44.237518892740106), 1956: (142.63816017773854, 44.237518892740106), 1957: (142.63816017773854, 44.10262083818142), 1958: (142.48781991641087, 44.37241694729879), 1959: (142.48781991641087, 44.507315001857464), 1960: (142.63816017773854, 44.507315001857464), 1961: (142.63816017773854, 44.37241694729879), 1962: (142.48781991641087, 44.64221305641614), 1963: (142.48781991641087, 44.77711111097482), 1964: (142.63816017773854, 44.77711111097482), 1965: (142.63816017773854, 44.64221305641614), 1966: (142.48781991641087, 44.912009165533505), 1967: (142.48781991641087, 45.04690722009218), 1968: (142.63816017773854, 44.912009165533505), 1969: (142.7885004390662, 42.21404807435992), 1970: (142.7885004390662, 42.3489461289186), 1971: (142.93884070039388, 42.3489461289186), 1972: (142.93884070039388, 42.21404807435992), 1973: (142.7885004390662, 42.483844183477274), 1974: (142.7885004390662, 42.618742238035956), 1975: (142.93884070039388, 42.618742238035956), 1976: (142.93884070039388, 42.483844183477274), 1977: (142.7885004390662, 42.75364029259464), 1978: (142.7885004390662, 42.888538347153315), 1979: (142.93884070039388, 42.888538347153315), 1980: (142.93884070039388, 42.75364029259464), 1981: (142.7885004390662, 43.02343640171199), 1982: (142.7885004390662, 43.15833445627067), 1983: (142.93884070039388, 43.15833445627067), 1984: (142.93884070039388, 43.02343640171199), 1985: (142.7885004390662, 43.293232510829355), 1986: (142.7885004390662, 43.42813056538803), 1987: (142.93884070039388, 43.42813056538803), 1988: (142.93884070039388, 43.293232510829355), 1989: (142.7885004390662, 43.56302861994671), 1990: (142.7885004390662, 43.69792667450539), 1991: (142.93884070039388, 43.69792667450539), 1992: (142.93884070039388, 43.56302861994671), 1993: (142.7885004390662, 43.83282472906407), 1994: (142.7885004390662, 43.96772278362275), 1995: (142.93884070039388, 43.96772278362275), 1996: (142.93884070039388, 43.83282472906407), 1997: (142.7885004390662, 44.10262083818142), 1998: (142.7885004390662, 44.237518892740106), 1999: (142.93884070039388, 44.237518892740106), 2000: (142.93884070039388, 44.10262083818142), 2001: (142.7885004390662, 44.37241694729879), 2002: (142.7885004390662, 44.507315001857464), 2003: (142.93884070039388, 44.507315001857464), 2004: (142.93884070039388, 44.37241694729879), 2005: (142.7885004390662, 44.64221305641614), 2006: (142.7885004390662, 44.77711111097482), 2007: (142.93884070039388, 44.64221305641614), 2008: (143.08918096172155, 42.07915001980124), 2009: (143.23952122304922, 42.07915001980124), 2010: (143.08918096172155, 42.21404807435992), 2011: (143.08918096172155, 42.3489461289186), 2012: (143.23952122304922, 42.3489461289186), 2013: (143.23952122304922, 42.21404807435992), 2014: (143.08918096172155, 42.483844183477274), 2015: (143.08918096172155, 42.618742238035956), 2016: (143.23952122304922, 42.618742238035956), 2017: (143.23952122304922, 42.483844183477274), 2018: (143.08918096172155, 42.75364029259464), 2019: (143.08918096172155, 42.888538347153315), 2020: (143.23952122304922, 42.888538347153315), 2021: (143.23952122304922, 42.75364029259464), 2022: (143.08918096172155, 43.02343640171199), 2023: (143.08918096172155, 43.15833445627067), 2024: (143.23952122304922, 43.15833445627067), 2025: (143.23952122304922, 43.02343640171199), 2026: (143.08918096172155, 43.293232510829355), 2027: (143.08918096172155, 43.42813056538803), 2028: (143.23952122304922, 43.42813056538803), 2029: (143.23952122304922, 43.293232510829355), 2030: (143.08918096172155, 43.56302861994671), 2031: (143.08918096172155, 43.69792667450539), 2032: (143.23952122304922, 43.69792667450539), 2033: (143.23952122304922, 43.56302861994671), 2034: (143.08918096172155, 43.83282472906407), 2035: (143.08918096172155, 43.96772278362275), 2036: (143.23952122304922, 43.96772278362275), 2037: (143.23952122304922, 43.83282472906407), 2038: (143.08918096172155, 44.10262083818142), 2039: (143.08918096172155, 44.237518892740106), 2040: (143.23952122304922, 44.237518892740106), 2041: (143.23952122304922, 44.10262083818142), 2042: (143.08918096172155, 44.37241694729879), 2043: (143.08918096172155, 44.507315001857464), 2044: (143.23952122304922, 44.507315001857464), 2045: (143.23952122304922, 44.37241694729879), 2046: (143.3898614843769, 42.618742238035956), 2047: (143.3898614843769, 42.75364029259464), 2048: (143.3898614843769, 42.888538347153315), 2049: (143.54020174570456, 42.888538347153315), 2050: (143.54020174570456, 42.75364029259464), 2051: (143.3898614843769, 43.02343640171199), 2052: (143.3898614843769, 43.15833445627067), 2053: (143.54020174570456, 43.15833445627067), 2054: (143.54020174570456, 43.02343640171199), 2055: (143.3898614843769, 43.293232510829355), 2056: (143.3898614843769, 43.42813056538803), 2057: (143.54020174570456, 43.42813056538803), 2058: (143.54020174570456, 43.293232510829355), 2059: (143.3898614843769, 43.56302861994671), 2060: (143.3898614843769, 43.69792667450539), 2061: (143.54020174570456, 43.69792667450539), 2062: (143.54020174570456, 43.56302861994671), 2063: (143.3898614843769, 43.83282472906407), 2064: (143.3898614843769, 43.96772278362275), 2065: (143.54020174570456, 43.96772278362275), 2066: (143.54020174570456, 43.83282472906407), 2067: (143.3898614843769, 44.10262083818142), 2068: (143.3898614843769, 44.237518892740106), 2069: (143.54020174570456, 44.237518892740106), 2070: (143.54020174570456, 44.10262083818142), 2071: (143.69054200703224, 42.75364029259464), 2072: (143.69054200703224, 42.888538347153315), 2073: (143.8408822683599, 42.888538347153315), 2074: (143.69054200703224, 43.02343640171199), 2075: (143.69054200703224, 43.15833445627067), 2076: (143.8408822683599, 43.15833445627067), 2077: (143.8408822683599, 43.02343640171199), 2078: (143.69054200703224, 43.293232510829355), 2079: (143.69054200703224, 43.42813056538803), 2080: (143.8408822683599, 43.42813056538803), 2081: (143.8408822683599, 43.293232510829355), 2082: (143.69054200703224, 43.56302861994671), 2083: (143.69054200703224, 43.69792667450539), 2084: (143.8408822683599, 43.69792667450539), 2085: (143.8408822683599, 43.56302861994671), 2086: (143.69054200703224, 43.83282472906407), 2087: (143.69054200703224, 43.96772278362275), 2088: (143.8408822683599, 43.96772278362275), 2089: (143.8408822683599, 43.83282472906407), 2090: (143.69054200703224, 44.10262083818142), 2091: (143.69054200703224, 44.237518892740106), 2092: (143.8408822683599, 44.237518892740106), 2093: (143.8408822683599, 44.10262083818142), 2094: (143.99122252968758, 43.02343640171199), 2095: (143.99122252968758, 43.15833445627067), 2096: (144.14156279101525, 43.15833445627067), 2097: (144.14156279101525, 43.02343640171199), 2098: (143.99122252968758, 43.293232510829355), 2099: (143.99122252968758, 43.42813056538803), 2100: (144.14156279101525, 43.42813056538803), 2101: (144.14156279101525, 43.293232510829355), 2102: (143.99122252968758, 43.56302861994671), 2103: (143.99122252968758, 43.69792667450539), 2104: (144.14156279101525, 43.69792667450539), 2105: (144.14156279101525, 43.56302861994671), 2106: (143.99122252968758, 43.83282472906407), 2107: (143.99122252968758, 43.96772278362275), 2108: (144.14156279101525, 43.96772278362275), 2109: (144.14156279101525, 43.83282472906407), 2110: (143.99122252968758, 44.10262083818142), 2111: (143.99122252968758, 44.237518892740106), 2112: (144.14156279101525, 44.10262083818142), 2113: (144.29190305234292, 43.02343640171199), 2114: (144.29190305234292, 43.15833445627067), 2115: (144.4422433136706, 43.15833445627067), 2116: (144.4422433136706, 43.02343640171199), 2117: (144.29190305234292, 43.293232510829355), 2118: (144.29190305234292, 43.42813056538803), 2119: (144.4422433136706, 43.42813056538803), 2120: (144.4422433136706, 43.293232510829355), 2121: (144.29190305234292, 43.56302861994671), 2122: (144.29190305234292, 43.69792667450539), 2123: (144.4422433136706, 43.69792667450539), 2124: (144.4422433136706, 43.56302861994671), 2125: (144.29190305234292, 43.83282472906407), 2126: (144.29190305234292, 43.96772278362275), 2127: (144.4422433136706, 43.96772278362275), 2128: (144.4422433136706, 43.83282472906407), 2129: (144.59258357499826, 43.02343640171199), 2130: (144.59258357499826, 43.15833445627067), 2131: (144.74292383632593, 43.15833445627067), 2132: (144.59258357499826, 43.293232510829355), 2133: (144.59258357499826, 43.42813056538803), 2134: (144.74292383632593, 43.42813056538803), 2135: (144.74292383632593, 43.293232510829355), 2136: (144.59258357499826, 43.56302861994671), 2137: (144.59258357499826, 43.69792667450539), 2138: (144.74292383632593, 43.69792667450539), 2139: (144.74292383632593, 43.56302861994671), 2140: (144.59258357499826, 43.83282472906407), 2141: (144.59258357499826, 43.96772278362275), 2142: (144.74292383632593, 43.96772278362275), 2143: (144.74292383632593, 43.83282472906407), 2144: (144.8932640976536, 43.15833445627067), 2145: (145.04360435898127, 43.15833445627067), 2146: (144.8932640976536, 43.293232510829355), 2147: (144.8932640976536, 43.42813056538803), 2148: (145.04360435898127, 43.42813056538803), 2149: (145.04360435898127, 43.293232510829355), 2150: (144.8932640976536, 43.56302861994671), 2151: (144.8932640976536, 43.69792667450539), 2152: (145.04360435898127, 43.69792667450539), 2153: (145.04360435898127, 43.56302861994671), 2154: (144.8932640976536, 43.83282472906407), 2155: (144.8932640976536, 43.96772278362275), 2156: (145.04360435898127, 43.96772278362275), 2157: (145.04360435898127, 43.83282472906407), 2158: (144.8932640976536, 44.10262083818142), 2159: (144.8932640976536, 44.237518892740106), 2160: (145.04360435898127, 44.237518892740106), 2161: (145.04360435898127, 44.10262083818142), 2162: (145.19394462030894, 43.293232510829355), 2163: (145.19394462030894, 43.42813056538803), 2164: (145.3442848816366, 43.293232510829355), 2165: (145.19394462030894, 43.56302861994671), 2166: (145.19394462030894, 43.69792667450539), 2167: (145.19394462030894, 44.10262083818142), 2168: (145.19394462030894, 44.237518892740106), 2169: (146.24428678526897, 44.5061047439825), 2170: (145.19394462030894, 44.37241694729879), 2171: (146.09125330671682, 44.51138287446291), 2172: (145.94249067257516, 44.50934869036335), 2173: (145.49462514296428, 43.293232510829355), 2174: (145.49462514296428, 43.42813056538803), 2175: (145.64496540429195, 43.42813056538803), 2176: (145.49462514296428, 43.83282472906407), 2177: (145.49462514296428, 43.96772278362275), 2178: (145.64496540429195, 43.96772278362275), 2179: (146.2493352594636, 44.373429474614916), 2180: (145.64496540429195, 44.237518892740106), 2181: (145.64496540429195, 44.10262083818142), 2182: (145.79530566561962, 44.10262083818142), 2183: (145.79530566561962, 44.237518892740106), 2184: (145.9456459269473, 44.237518892740106), 2185: (145.79530566561962, 44.37241694729879), 2186: (146.09662167418418, 44.372921010962), 2187: (145.9456459269473, 44.37241694729879)}
# Container for data
data_to_dump = {'prefecture_city_list': prefecture_city_list, 'prefecture_area_dict': prefecture_area_dict,
                'prefecture_pop_dict': prefecture_pop_dict, 'tile_pdf_dict': tile_pdf_dict,
                  'prefecture_tile_dict': prefecture_tile_dict, 'normalized_tile_pdf_dict': normalized_tile_pdf_dict,
                  'tile_dict': tile_dict}
with open('./population/relevant_data/pickleFiles/pop_pickle.pkl', 'wb') as file:
      data_list = pickle.dump(data_to_dump,file)







  