import difflib

# دالة لتحويل الجملة إلى كلمات صغيرة
def lower_super_space(sentence):
    return sentence.lower().split()

# قائمة الأفعال المساعدة
auxiliary_verbs = ['is', 'am', 'are', 'was', 'were', 'has', 'have', 'had', 'will', 'would', 'shall', 'should', 'can', 'could', 'may', 'might', 'be', 'been']

# قائمة الضمائر
pronouns = ['i', 'you', 'he', 'she', 'it', 'we', 'they', 
            'myself', 'yourself', 'himself', 'herself', 'itself', 'ourselves', 'yourselves', 'themselves',
            'my', 'your', 'his', 'her', 'its', 'our', 'their']

# قائمة كلمات الزمن
time_words = ['yesterday', 'today', 'tomorrow', 'now']

# قائمة الكلمات الصحيحة لتصحيح الأخطاء الإملائية
common_words = ['go', 'went', 'want', 'wanted', 'see', 'saw', 'read', 'reading']

# دالة لتصحيح الأخطاء الإملائية
def correct_spelling(word):
    closest_matches = difflib.get_close_matches(word, common_words + time_words)
    return closest_matches[0] if closest_matches else word

# دالة لتحليل وتصحيح الجملة
def analyze_and_correct_sentence(sentence):
    words = lower_super_space(sentence)  # تحويل الجملة إلى كلمات صغيرة
    
    subject = None
    verb = None
    aux_verb = None
    obj = None
    time_word = None
    corrections = []  # قائمة التصحيحات
    
    # تحليل الكلمات بحثًا عن الفاعل، الفعل، والمفعول
    for i, word in enumerate(words):
        corrected_word = correct_spelling(word)  # تصحيح الأخطاء الإملائية
        if corrected_word != word:
            corrections.append(f"Corrected '{word}' to '{corrected_word}'")

        if corrected_word in pronouns and not subject:
            subject = corrected_word  # تحديد الفاعل
        elif corrected_word in auxiliary_verbs and not aux_verb:
            aux_verb = corrected_word  # تحديد الفعل المساعد
        elif corrected_word.isalpha() and not verb:
            verb = corrected_word  # تحديد الفعل الرئيسي
        elif corrected_word in time_words:
            time_word = corrected_word  # تحديد كلمة الزمن
        elif verb and not obj:
            obj = corrected_word  # تحديد المفعول

    # التحقق من النتائج النهائية
    if corrections:
        print("Corrections:")
        for correction in corrections:
            print(correction)

    # عرض الجملة المحللة
    print(f"Main Clause: {' '.join(words)}")
    print(f"- Subject: '{subject if subject else 'None'}' (This is the person or thing doing the action)")
    print(f"- Main Verb: '{verb if verb else 'None'}' (This is the main action in the sentence)")
    if obj:
        print(f"- Object: '{obj}' (This is the thing receiving the action)")
    if time_word:
        print(f"- Time word: '{time_word}' (This indicates the time of the action)")

    # تحقق من الجملة الصحيحة
    if subject is None or verb is None:
        print("The sentence seems incomplete or incorrect. Make sure it includes both a subject and a verb.")

# برنامج تفاعلي لتعليم الطلاب
while True:
    sentence = input("Enter your sentence (or type 'exit' to stop): ")
    if sentence.lower() == 'exit':
        break
    analyze_and_correct_sentence(sentence)
