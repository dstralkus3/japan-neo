import pickle
ap_dict ={'Japan National Stadium': ['35.67782', '139.71454'], 'Nissan Stadium': ['35.50994', '139.60639'], 'Saitama Stadium': ['35.90372', '139.7174'], 'Tokyo Dome': ['35.70563', '139.75189'], 'Kyocera Dome Osaka': ['34.66928', '135.47614'], 'Sapparo Dome': ['34.66928', '135.47614'], 'Fukuoka PayPay Dome': ['33.59539', '130.36212'], 'Shizuoka Stadium': ['34.74345', '137.97076'], 'Ajinomoto Stadium': ['35.66405', '139.52717'], 'Nagoya Dome': ['35.186', '136.94739'], 'Q&A Stadium Miyagi': ['38.33543', '140.95056'], 'Koshien Stadium': ['34.72121', '135.36165'], 'Yanmar Stadium Nagai': ['34.61404', '135.51859'], 'Toyota Stadium': ['35.08447', '137.17091'], 'Kobe Universiade Memorial': ['34.68238', '135.08034'], 'Showa Denko Dome': ['33.20078', '131.6575'], 'Denka Big Swan Stadium': ['37.88254', '139.05916'], 'Kashima Football Stadium': ['35.99201', '140.64016'], 'Edion Stadium': ['34.44074', '132.39436'], 'Noevir Stadium': ['34.65681', '135.16962'], 'Belluna Dome': ['35.76901', '139.42019'], 'Mazda Stadium': ['34.39188', '132.48457'], 'Todoroki Athletics Stadium': ['35.5858', '139.65272'], 'Hanazono Rugby Stadium': ['34.66895', '135.62632'], 'Gifu Nagaragawa Stadium': ['35.44131', '136.76609'], 'Toyama Athletics Stadium': ['36.625', '137.19569'], 'Kanseki Stadium': ['36.515', '139.85752'], 'Kochi Haruno Stadium': ['33.50995', '133.50135'], 'Matsumoto Daira Stadium': ['36.25814', '137.98862'], 'Chichibunomiya Rugby ': ['35.67265', '139.71833'], 'Ekimae Stadium': ['33.37167', '130.52024'], 'Matsue Athletics Stadium': ['35.43739', '133.0639'], 'Akita Prefectural Stadium': ['39.72147', '140.09986'], 'Fukui Prefectural Stadium': ['36.05188', '136.18272'], 'Kitakami Stadium': ['39.25805', '141.09602'], 'Best Denki Stadium': ['33.58589', '130.46079'], 'ND Soft Stadium': ['38.33564', '140.37846'], 'Kamoike Ballpark': ['31.56436', '130.55775'], 'Toho Stadium': ['37.72323', '140.36137'], 'Sapparo Atsubetsu': ['43.019', '141.46407'], 'Kakuhiro Group Athletics': ['40.83889', '140.84144'], 'Takebishi Stadium': ['34.99345', '135.71396'], 'Pocarisweat Stadium': ['34.16827', '134.61771'], 'IAI Stadium': ['34.98432', '138.4813'], 'Transcosmos Stadium': ['32.83862', '130.03942'], 'Soyu Stadium': ['39.72154', '140.0958'], 'Komazawa Olympic Stadium': ['35.62557', '139.66364'], 'Chiyodai Baseball Stadium': ['41.78525', '140.74672'], 'Hinata Stadium': ['31.82437', '131.44806'], 'Kashiwanoha Stadium': ['35.89774', '139.93624'], 'Ningineer Stadium': ['33.76823', '132.79759'], 'Ishin Me-Life Stadium': ['34.15445', '131.4375'], 'Ota Athletics Stadium': ['36.27539', '139.39692'], 'Obihiro Athletics Stadium': ['42.89413', '143.14523'], 'Hanasaki Sports Park': ['43.79116', '142.3753'], 'Nagaoka Athletics Stadium': ['37.44636', '138.79768'], 'US Embassy ': ['35.6688', '139.74332'], 'US Consolate General Osaka-Kobe': ['34.69679', '135.50184'], 'US Consolate General Sapparo': ['43.05634', '141.31369'], 'US Consolate Fukuoka': ['33.5881', '130.37302'], 'US Consolate Nagoya': ['35.17273', '136.89028'], 'US army Camp Zama': ['35.48958', '139.39573'], 'Yokota Air Base': ['35.74283', '139.33842'], 'Misawa Air Base': ['40.69892', '141.37457'], 'MCAS Iwakuni': ['34.14283', '132.22518'], 'Yokosuka Navy Base': ['35.28441', '139.66578'], 'Atsugi Navy Base': ['35.45672', '139.44415'], 'Sasebo Navy Base': ['33.16715', '129.71534']}
data_to_dump = {'ap_dict': ap_dict}

with open('./assemblyPoints/relevant_data/pickleFiles/ap_pickle.pkl', 'wb') as file:
        data_list = pickle.dump(data_to_dump, file)
