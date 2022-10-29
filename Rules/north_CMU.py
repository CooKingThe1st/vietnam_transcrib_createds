#coding: utf-8

onsets = {'b': 'b', 't': 't', 'th': 'th', 'đ': 'đ', 'ch': 'ch','qu': 'qu', 'kh': 'kh', 'g': 'g', 'l': 'l', 'm': 'm', 'n': 'n', 'ngh': 'ngh', 'nh': 'nh', 'ng': 'ng', 'ph': 'ph', 'v': 'v', 'x': 'x', 'd': 'd', 'h': 'h', 'p': 'p', 'q': 'q', 'gi': 'gi', 'tr': 'tr', 'k': 'k', 'c': 'c', 'gh': 'gh', 'r': 'r', 's': 's'}

nuclei = {'a': 'a', 'á': 'á', 'à': 'à', 'ả': 'ả', 'ã': 'ã', 'ạ': 'ạ', 'â': 'â', 'ấ': 'ấ', 'ầ': 'ầ', 'ẩ': 'ẩ', 'ẫ': 'ẫ', 'ậ': 'ậ', 'ă': 'ă', 'ắ': 'ắ', 'ằ': 'ằ', 'ẳ': 'ẳ', 'ẵ': 'ẵ', 'ặ': 'ặ', 'e': 'e', 'é': 'é', 'è': 'è', 'ẻ': 'ẻ', 'ẽ': 'ẽ', 'ẹ': 'ẹ', 'ê': 'ê', 'ế': 'ế', 'ề': 'ề', 'ể': 'ể', 'ễ': 'ễ', 'ệ': 'ệ', 'i': 'i', 'í': 'í', 'ì': 'ì', 'ỉ': 'ỉ', 'ĩ': 'ĩ', 'ị': 'ị', 'o': 'o', 'ó': 'ó', 'ò': 'ò', 'ỏ': 'ỏ', 'õ': 'õ', 'ọ': 'ọ', 'ô': 'ô', 'ố': 'ố', 'ồ': 'ồ', 'ổ': 'ổ', 'ỗ': 'ỗ', 'ộ': 'ộ', 'ơ': 'ơ', 'ớ': 'ớ', 'ờ': 'ờ', 'ở': 'ở', 'ỡ': 'ỡ', 'ợ': 'ợ', '': '', 'ú': 'ú', 'ù': 'ù', 'ủ': 'ủ', 'ũ': 'ũ', 'ụ': 'ụ', 'ư': 'ư', 'ứ': 'ứ', 'ừ': 'ừ', 'ử': 'ử', 'ữ': 'ữ', 'ự': 'ự', 'y': 'y', 'ý': 'ý', 'ỳ': 'ỳ', 'ỷ': 'ỷ', 'ỹ': 'ỹ', 'ỵ': 'ỵ', 'eo': 'eo', 'éo': 'éo', 'èo': 'èo', 'ẻo': 'ẻo', 'ẽo': 'ẽo', 'ẹo': 'ẹo', 'ia': 'ia', 'ía': 'ía', 'ìa': 'ìa', 'ỉa': 'ỉa', 'ĩa': 'ĩa', 'ịa': 'ịa', 'iá': 'iá', 'ià': 'ià', 'iả': 'iả', 'iã': 'iã', 'iạ': 'iạ', 'iê': 'iê', 'iế': 'iế', 'iề': 'iề', 'iể': 'iể', 'iễ': 'iễ', 'iệ': 'iệ', 'oo': 'oo', 'óo': 'óo', 'òo': 'òo', 'ỏo': 'ỏo', 'õo': 'õo', 'ọo': 'ọo', 'oó': 'oó', 'oò': 'oò', 'oỏ': 'oỏ', 'oõ': 'oõ', 'oọ': 'oọ', 'ôô': 'ôô', 'ốô': 'ốô', 'ồô': 'ồô', 'ổô': 'ổô', 'ỗô': 'ỗô', 'ộô': 'ộô', 'ôố': 'ôố', 'ôồ': 'ôồ', 'ôổ': 'ôổ', 'ôỗ': 'ôỗ', 'ôộ': 'ôộ', 'ua': 'ua', 'úa': 'úa', 'ùa': 'ùa', 'ủa': 'ủa', 'ũa': 'ũa', 'ụa': 'ụa', 'uô': 'uô', 'uố': 'uố', 'uồ': 'uồ', 'uổ': 'uổ', 'uỗ': 'uỗ', 'uộ': 'uộ', 'ưa': 'ưa', 'ứa': 'ứa', 'ừa': 'ừa', 'ửa': 'ửa', 'ữa': 'ữa', 'ựa': 'ựa', 'ươ': 'ươ', 'ướ': 'ướ', 'ườ': 'ườ', 'ưở': 'ưở', 'ưỡ': 'ưỡ', 'ượ': 'ượ', 'yê': 'yê', 'yế': 'yế', 'yề': 'yề', 'yể': 'yể', 'yễ': 'yễ', 'yệ': 'yệ', 'uơ': 'uơ', 'uở': 'uở', 'uờ': 'uờ', 'uỡ': 'uỡ', 'uợ': 'uợ', 'u': 'u'}
				         		         
offglides =  {'ai': 'ai', 'ái': 'ái', 'ài': 'ài', 'ải': 'ải', 'ãi': 'ãi', 'ại': 'ại', 'ay': 'ay', 'áy': 'áy', 'ày': 'ày', 'ảy': 'ảy', 'ãy': 'ãy', 'ạy': 'ạy', 'ao': 'ao', 'áo': 'áo', 'ào': 'ào', 'ảo': 'ảo', 'ão': 'ão', 'ạo': 'ạo', 'a': 'a', 'á': 'á', 'à': 'à', 'ả': 'ả', 'ã': 'ã', 'ạ': 'ạ', 'ây': 'ây', 'ấy': 'ấy', 'ầy': 'ầy', 'ẩy': 'ẩy', 'ẫy': 'ẫy', 'ậy': 'ậy', 'â': 'â', 'ấ': 'ấ', 'ầ': 'ầ', 'ẩ': 'ẩ', 'ẫ': 'ẫ', 'ậ': 'ậ', 'eo': 'eo', 'éo': 'éo', 'èo': 'èo', 'ẻo': 'ẻo', 'ẽo': 'ẽo', 'ẹo': 'ẹo', 'i': 'i', 'í': 'í', 'ì': 'ì', 'ỉ': 'ỉ', 'ĩ': 'ĩ', 'ị': 'ị', 'oi': 'oi', 'ói': 'ói', 'òi': 'òi', 'ỏi': 'ỏi', 'õi': 'õi', 'ọi': 'ọi', 'ôi': 'ôi', 'ối': 'ối', 'ồi': 'ồi', 'ổi': 'ổi', 'ỗi': 'ỗi', 'ội': 'ội', 'ui': 'ui', 'úi': 'úi', 'ùi': 'ùi', 'ủi': 'ủi', 'ũi': 'ũi', 'ụi': 'ụi', 'uy': 'uy', 'úy': 'úy', 'ùy': 'ùy', 'ủy': 'ủy', 'ũy': 'ũy', 'ụy': 'ụy', 'ơi': 'ơi', 'ới': 'ới', 'ời': 'ời', 'ởi': 'ởi', 'ỡi': 'ỡi', 'ợi': 'ợi', 'ưi': 'ưi', 'ứi': 'ứi', 'ừi': 'ừi', 'ửi': 'ửi', 'ữi': 'ữi', 'ựi': 'ựi', 'ư': 'ư', 'ứ': 'ứ', 'ừ': 'ừ', 'ử': 'ử', 'ữ': 'ữ', 'ự': 'ự', 'iê': 'iê', 'iế': 'iế', 'iề': 'iề', 'iể': 'iể', 'iễ': 'iễ', 'iệ': 'iệ', 'yê': 'yê', 'yế': 'yế', 'yề': 'yề', 'yể': 'yể', 'yễ': 'yễ', 'yệ': 'yệ', 'uôi': 'uôi', 'uối': 'uối', 'uồi': 'uồi', 'uổi': 'uổi', 'uỗi': 'uỗi', 'uội': 'uội', 'ươi': 'ươi', 'ưới': 'ưới', 'ười': 'ười', 'ưởi': 'ưởi', 'ưỡi': 'ưỡi', 'ượi': 'ượi', 'ươ': 'ươ', 'ướ': 'ướ', 'ườ': 'ườ', 'ưở': 'ưở', 'ưỡ': 'ưỡ', 'ượ': 'ượ', 'au': 'au', 'áu': 'áu', 'àu': 'àu', 'ảu': 'ảu', 'ãu': 'ãu', 'ạu': 'ạu', 'âu': 'âu', 'ấu': 'ấu', 'ầu': 'ầu', 'ẩu': 'ẩu', 'ẫu': 'ẫu', 'ậu': 'ậu', 'êu': 'êu', 'ếu': 'ếu', 'ều': 'ều', 'ểu': 'ểu', 'ễu': 'ễu', 'ệu': 'ệu', 'iu': 'iu', 'íu': 'íu', 'ìu': 'ìu', 'ỉu': 'ỉu', 'ĩu': 'ĩu', 'ịu': 'ịu', 'ưu': 'ưu', 'ứu': 'ứu', 'ừu': 'ừu', 'ửu': 'ửu', 'ữu': 'ữu', 'ựu': 'ựu', 'iêu': 'iêu', 'iếu': 'iếu', 'iều': 'iều', 'iểu': 'iểu', 'iễu': 'iễu', 'iệu': 'iệu', 'yêu': 'yêu', 'yếu': 'yếu', 'yều': 'yều', 'yểu': 'yểu', 'yễu': 'yễu', 'yệu': 'yệu', 'ươu': 'ươu', 'ướu': 'ướu', 'ườu': 'ườu', 'ưởu': 'ưởu', 'ưỡu': 'ưỡu', 'ượu': 'ượu'}
				
onglides =   {'oa': 'oa', 'oá': 'oá', 'oà': 'oà', 'oả': 'oả', 'oã': 'oã', 'oạ': 'oạ', 'óa': 'óa', 'òa': 'òa', 'ỏa': 'ỏa', 'õa': 'õa', 'ọa': 'ọa', 'oă': 'oă', 'oắ': 'oắ', 'oằ': 'oằ', 'oẳ': 'oẳ', 'oẵ': 'oẵ', 'oặ': 'oặ', 'oe': 'oe', 'oé': 'oé', 'oè': 'oè', 'oẻ': 'oẻ', 'oẽ': 'oẽ', 'oẹ': 'oẹ', 'óe': 'óe', 'òe': 'òe', 'ỏe': 'ỏe', 'õe': 'õe', 'ọe': 'ọe', 'ua': 'ua', 'uá': 'uá', 'uà': 'uà', 'uả': 'uả', 'uã': 'uã', 'uạ': 'uạ', 'uă': 'uă', 'uắ': 'uắ', 'uằ': 'uằ', 'uẳ': 'uẳ', 'uẵ': 'uẵ', 'uặ': 'uặ', 'uâ': 'uâ', 'uấ': 'uấ', 'uầ': 'uầ', 'uẩ': 'uẩ', 'uẫ': 'uẫ', 'uậ': 'uậ', 'ue': 'ue', 'ué': 'ué', 'uè': 'uè', 'uẻ': 'uẻ', 'uẽ': 'uẽ', 'uẹ': 'uẹ', 'uê': 'uê', 'uế': 'uế', 'uề': 'uề', 'uể': 'uể', 'uễ': 'uễ', 'uệ': 'uệ', 'uơ': 'uơ', 'uớ': 'uớ', 'uờ': 'uờ', 'uở': 'uở', 'uỡ': 'uỡ', 'uợ': 'uợ', 'uy': 'uy', 'uý': 'uý', 'uỳ': 'uỳ', 'uỷ': 'uỷ', 'uỹ': 'uỹ', 'uỵ': 'uỵ', 'uya': 'uya', 'uyá': 'uyá', 'uyà': 'uyà', 'uyả': 'uyả', 'uyã': 'uyã', 'uyạ': 'uyạ', 'uyê': 'uyê', 'uyế': 'uyế', 'uyề': 'uyề', 'uyể': 'uyể', 'uyễ': 'uyễ', 'uyệ': 'uyệ', 'uyú': 'uyú', 'uyù': 'uyù', 'uyủ': 'uyủ', 'uyũ': 'uyũ', 'uyụ': 'uyụ', 'oen': 'oen', 'oén': 'oén', 'oèn': 'oèn', 'oẻn': 'oẻn', 'oẽn': 'oẽn', 'oẹn': 'oẹn', 'oet': 'oet', 'oét': 'oét', 'oèt': 'oèt', 'oẻt': 'oẻt', 'oẽt': 'oẽt', 'oẹt': 'oẹt', 'uyu': 'uyu', 'uýu': 'uýu', 'uỳu': 'uỳu', 'uỷu': 'uỷu', 'uỹu': 'uỹu', 'uỵu': 'uỵu'}

onoffglides = {'oe': 'oe', 'oé': 'oé', 'oè': 'oè', 'oẻ': 'oẻ', 'oẽ': 'oẽ', 'oẹ': 'oẹ', 'oai': 'oai', 'oái': 'oái', 'oài': 'oài', 'oải': 'oải', 'oãi': 'oãi', 'oại': 'oại', 'oay': 'oay', 'oáy': 'oáy', 'oày': 'oày', 'oảy': 'oảy', 'oãy': 'oãy', 'oạy': 'oạy', 'oao': 'oao', 'oáo': 'oáo', 'oào': 'oào', 'oảo': 'oảo', 'oão': 'oão', 'oạo': 'oạo', 'oeo': 'oeo', 'oéo': 'oéo', 'oèo': 'oèo', 'oẻo': 'oẻo', 'oẽo': 'oẽo', 'oẹo': 'oẹo', 'óeo': 'óeo', 'òeo': 'òeo', 'ỏeo': 'ỏeo', 'õeo': 'õeo', 'ọeo': 'ọeo', 'ueo': 'ueo', 'uéo': 'uéo', 'uèo': 'uèo', 'uẻo': 'uẻo', 'uẽo': 'uẽo', 'uẹo': 'uẹo', 'uai': 'uai', 'uái': 'uái', 'uài': 'uài', 'uải': 'uải', 'uãi': 'uãi', 'uại': 'uại', 'uay': 'uay', 'uáy': 'uáy', 'uày': 'uày', 'uảy': 'uảy', 'uãy': 'uãy', 'uạy': 'uạy', 'uây': 'uây', 'uấy': 'uấy', 'uầy': 'uầy', 'uẩy': 'uẩy', 'uẫy': 'uẫy', 'uậy': 'uậy'}

codas = {'p': 'p', 't': 't', 'c': 'c', 'm': 'm', 'n': 'n', 'ng': 'ng', 'nh': 'nh', 'ch': 'ch'}
tones   =     { 'á' : 24, 'à' : 32, 'ả' : 312, 'ã' : '35g', 'ạ' : '21g', 
				'ấ' : 24, 'ầ' : 32, 'ẩ' : 312, 'ẫ' : '35g', 'ậ' : '21g',
				'ắ' : 24, 'ằ' : 32, 'ẳ' : 312, 'ẵ' : '35g', 'ặ' : '21g',
				'é' : 24, 'è' : 32, 'ẻ' : 312, 'ẽ' : '35g', 'ẹ' : '21g',
				'ế' : 24, 'ề' : 32, 'ể' : 312, 'ễ' : '35g', 'ệ' : '21g',
				'í' : 24, 'ì' : 32, 'ỉ' : 312, 'ĩ' : '35g', 'ị' : '21g',
				'ó' : 24, 'ò' : 32, 'ỏ' : 312, 'õ' : '35g', 'ọ' : '21g',
				'ố' : 24, 'ồ' : 32, 'ổ' : 312, 'ỗ' : '35g', 'ộ' : '21g',
				'ớ' : 24, 'ờ' : 32, 'ở' : 312, 'ỡ' : '35g', 'ợ' : '21g',
				'ú' : 24, 'ù' : 32, 'ủ' : 312, 'ũ' : '35g', 'ụ' : '21g',
				'ứ' : 24, 'ừ' : 32, 'ử' : 312, 'ữ' : '35g', 'ự' : '21g',
				'ý' : 24, 'ỳ' : 32, 'ỷ' : 312, 'ỹ' : '35g', 'ỵ' : '21g',
			  }
# used to use \u02C0 for the unicode raised glottal character

tones_p =     { 'á' : 5, 'à' : 2, 'ả' : 4, 'ã' : 3, 'ạ' : 6, 
				'ấ' : 5, 'ầ' : 2, 'ẩ' : 4, 'ẫ' : 3, 'ậ' : 6,
				'ắ' : 5, 'ằ' : 2, 'ẳ' : 4, 'ẵ' : 3, 'ặ' : 6,
				'é' : 5, 'è' : 2, 'ẻ' : 4, 'ẽ' : 3, 'ẹ' : 6,
				'ế' : 5, 'ề' : 2, 'ể' : 4, 'ễ' : 3, 'ệ' : 6,
				'í' : 5, 'ì' : 2, 'ỉ' : 4, 'ĩ' : 3, 'ị' : 6,
				'ó' : 5, 'ò' : 2, 'ỏ' : 4, 'õ' : 3, 'ọ' : 6,
				'ố' : 5, 'ồ' : 2, 'ổ' : 4, 'ỗ' : 3, 'ộ' : 6,
				'ớ' : 5, 'ờ' : 2, 'ở' : 4, 'ỡ' : 3, 'ợ' : 6,
				'ú' : 5, 'ù' : 2, 'ủ' : 4, 'ũ' : 3, 'ụ' : 6,
				'ứ' : 5, 'ừ' : 2, 'ử' : 4, 'ữ' : 3, 'ự' : 6,
				'ý' : 5, 'ỳ' : 2, 'ỷ' : 4, 'ỹ' : 3, 'ỵ' : 6,
			  }
			  
gi = {'gi': 'gi', 'gí': 'gí', 'gì': 'gì', 'gĩ': 'gĩ', 'gị': 'gị'}
qu = {'quy': 'quy', 'qúy': 'qúy', 'qùy': 'qùy', 'qủy': 'qủy', 'qũy': 'qũy', 'qụy': 'qụy'}
