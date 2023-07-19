import pickle

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
with open('./population/data.pkl', 'wb') as file:
    pickle.dump(prefecture_city_list, file)