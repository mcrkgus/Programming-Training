#컴퓨터프로그래밍 과제 
#대통령 연설문을 인터넷에서 검색 후 문자열로 저장 
#연설문 속의 단어를 찾아 단어별 빈도수 카운트해서 화면에 출력한다. 
#예를 들어 '꽃'이 10번 나오면 폰트크기 10으로 출력하거나한다. 
#키워드는 '민주', '국민', '오월의', '사랑하는', '자유민주주의', '여러분', '하나'로 정한다.



import turtle
import random

def getXYAS():
    x, y, angle, size = 0, 0, 0, 0
    x = random.randint(-250, 250)
    y = random.randint(-250, 250)
    size = random.randint(10, 50)
    return x, y, size


#koreaStr = '존경하는 국민 여러분 , 518 민주화운동 유공자와 유가족 여러분 , 오늘 우리는 43년 전, 자유민주주의 와 인권의 가치를 피로써 지켜낸 오월의 항거를 기억하고, 민주 영령들을 기리기 위해 이 자리에 함께 섰습니다. 민주 영령들의 희생과 용기에 깊은 경의를 표하며 명복을 빕니다. 오랜 세월 그날의 아픔을 가슴에 묻고 계신 5.18 민주화 유공자와 유가족분들께 깊은 위로의 말씀을 드립니다. 이 땅의 자유민주주의 는 저절로 얻어진 것이 아닙니다. 수많은 분들의 희생과 헌신으로 지켜낸 것입니다.'
koreaStr = """존경하는 국민 여러분, 518 민주화운동 유공자와 유가족 여러분, 오늘 우리는 43년 전, 자유민주주의 와 인권의 가치를 피로써 지켜낸 오월의 항거를 기억하고, 민주 영령들을 기리기 위해 이 자리에 함께 섰습니다.
민주 영령들의 희생과 용기에 깊은 경의를 표하며 명복을 빕니다.
오랜 세월 그날의 아픔을 가슴에 묻고 계신 5.18 민주화 유공자와 유가족분들께 깊은 위로의 말씀을 드립니다.
이 땅의 자유민주주의 는 저절로 얻어진 것이 아닙니다. 수많은 분들의 희생과 헌신으로 지켜낸 것입니다.
광주는 자유민주주의 와 인권의 가치를 지켜낸 역사의 현장이었습니다.
오월의 정신은 우리 자유민주주의 헌법 정신 그 자체이고, 우리가 반드시 계승해야 할 소중한 자산입니다. 우리를 하나 로 묶는 구심체입니다.
그리고 오월의 정신은 우리에게 자유민주주의 를 지키기 위한 실천을 명령하고 있습니다.
우리가 오월의 정신을 잊지 않고 계승한다면 우리는 자유와 민주주의를 위협하는 모든 세력과 도전에 당당히 맞서 싸워야 하고 그런 실천적 용기를 가져야 합니다.
민주주의의 위기를 초래하는 안팎의 도전에 맞서 투쟁하지 않는다면 오월의 정신을 말하기 부끄러울 것입니다.
사랑하는 국민 여러분, 그리고 자랑스러운 광주시민과 전남도민 여러분
오월의 정신은 자유와 창의, 그리고 혁신을 통해 광주와 호남의 산업적 성취와 경제 발전에 의해 승화되고 완성됩니다.
저는 광주와 호남이 자유와 성취를 바탕으로 A와 첨단 과학 기술의 고도화를 이루어 내 고 이러한 성취를 미래 세대에게 계승시킬 수 있도록 대통령으로서 제대로 뒷받침하겠습니다.
오늘 이 자리에 '오월의 어머니'들이 함께 하고 계십니다.
사랑하는 남편, 자식, 형제를 잃은 한을 가슴에 안고서도 오월의 정신이 빛을 잃지 않도록 일생을 바치신 분들입니다.
애통한 세월을 감히 헤아릴 수 없지만, 희망을 잃지 않고 살아가시는 분들의 용기에 다시 한번 깊이 감사드립니다. 
존경하는 국민 여러분 
사랑하는 광주시민과 전남도민 여러분,
우리는 모두 오월의 정신으로 위협과 도전에 직면한 우리의 자유민주주의 를 지키고 실천하며
창의와 혁신의 정신으로 산업의 고도화, 경제의 번영을 이루어 내야 합니다.
그것이 오월의 정신을 구현하는 길이고 민주영령들께 보답하는 길입니다.
오월의 정신으로 우리는 모두 하나 가 되었습니다.
오월의 정신 아래 우리는 모두 하나 입니다.
민주 영령들의 안식을 기원합니다. """


keywords = {
    '국민': 0,
    '오월의': 0,
    '여러분' : 0,
    '사랑하는' : 0,
    '자유민주주의' : 0,
    '민주' : 0,
    '하나' : 0
}
turtle.shape('turtle')
turtle.setup(550, 550)
turtle.screensize(500, 500)
turtle.penup()
turtle.speed(30)


for word in koreaStr.split():
    if word in keywords:
        keywords[word] += 1
 
color = 'black'


for word in koreaStr.split() :
    tX, tY, txtSize = getXYAS()
    if word in keywords :
        if word == '국민' and keywords[word] >= 2:
            turtle.write(word, font=('맑은고딕', 25, 'bold'))
        elif word == '오월의' and keywords[word] >= 7:
            turtle.write(word, font=('맑은고딕', 30, 'bold'))
        elif word == '여러분'  and keywords[word] >= 1:
            turtle.write(word, font=('맑은고딕', 35, 'bold'))
        elif word == '사랑하는' and keywords[word] >= 2 :
            turtle.write(word, font=('맑은고딕', 40, 'bold'))
        elif word == '자유민주주의' and keywords[word] >= 4 :
            turtle.write(word, font=('맑은고딕', 45, 'bold'))
        elif word == '민주' and keywords[word] >= 2 :
            turtle.write(word, font=('맑은고딕', 50, 'bold'))
        elif word == '하나' and keywords[word] >= 1 :
            turtle.write(word, font=('맑은고딕', 55, 'bold'))
        turtle.pencolor(color)
        turtle.write(word, font=('맑은고딕', 5, 'bold'))
    else:
        turtle.write(word, font=('맑은고딕', 5, 'normal'))
    turtle.penup()
    turtle.goto(tX, tY)
turtle.done()
print(keywords)