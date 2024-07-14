# 如果要运行图片处理工具
# 在run后面输入:(空格)--server.enableXsrfProtection=false
'''我的主页'''
import streamlit as st
from PIL import Image

page = st.sidebar.radio('我的首页', ['我的兴趣推荐', '我的图片处理工具', '我的智慧词典', '我的留言区', '猜一猜'])

# 小程序
def image_change(img, r_c, g_c, b_c):
    # 图片处理工具
    width, height = img.size
    img_array = img.load()
    for x in range(width):
        for y in range(height):
            r = img_array[x,y][r_c]
            g = img_array[x,y][g_c]
            b = img_array[x,y][b_c]
            img_array[x,y] = (r, g, b)
    return img


# 页面 
def page_1():
    # 我的兴趣推荐
    with open('music.mp3','rb') as f:
        mymp3 = f.read()
    st.audio(mymp3, format = 'audio/mp3', start_time = 0)
    st.write(':train:我爱旅行(bu_shi_wo_pai_de):')
    st.write(':orange[难忘的旅行、难得的景色]')
    st.image('挪威1.jpg')
    
    # 季节互动
    season = st.text_input('这是什么季节(请输入英文)')
    if season == 'winter':
        st.snow()

def page_2():
    # 我的图片处理工具
    st.write(':sunglasses:图片换色小程序:sunglasses')
    uploaded_file = st.file_uploader('上传图片', type = ['png','jpeg','jpg'])
    if uploaded_file:
        name = uploaded_file.name
        type = uploaded_file.type
        size = uploaded_file.size

        img = Image.open(uploaded_file)
        st.image(img)
        # st.image(image_change(img, 1, 2, 0))
        tab1, tab2, tab3, tab4= st.tabs(['你猜', '你猜', '你猜', '你猜'])
        with tab1:
            st.image(image_change(img, 0, 2, 1))
        with tab2:
            st.image(image_change(img, 1, 0, 2))
        with tab3:
            st.image(image_change(img, 2, 0, 1))
        with tab4:
            st.image(image_change(img, 2, 1, 0))

def page_3():
    # 我的智慧词典
    st.write(':book:智能词典:book')

    # 遍历词典
    with open('words_space.txt', 'r', encoding='utf-8') as f:
        word_list = f.read().split('\n')
    for i in range(len(word_list)):
        word_list[i] = word_list[i].split('#')

    word_dict = {}
    for j in word_list:
        word_dict[j[1]] = [j[0], j[2]]
    # 查询次数
    with open('check_out_time.txt','r',encoding='utf-8') as f:
        times_list = f.read().split('\n')
    for i in range(len(times_list)):
        times_list[i] = times_list[i].split('#')

    times_dict = {}
    if len(times_list[0]) > 1:
        for j in times_list:
            times_dict[j[0]] = int(j[1])
    # 创建输入框
    word = st.text_input('请输入要查询的单词')
    if word in word_dict:
        st.write(word_dict[word][1])
        # 更新次数
        n = word_dict[word][0]
        if n in times_dict:
            times_dict[n] += 1
        else:
            times_dict[n] = 1
        st.write('查询次数:' + str(times_dict[n]))

        with open('check_out_time.txt', 'w', encoding='utf-8') as f:
            message = ''
            for k, v in times_dict.items():
                message += str(k) + '#' + str(v) + '\n'
            message = message[:-1]
            f.write(message)
           
def page_4():
    # 我的留言区
    st.write('我的留言区')
    with open('leave_messages.txt', 'r', encoding='utf-8') as f:
        messages_list = f.read().split('\n')
    for i in range(len(messages_list)):
        messages_list[i] = messages_list[i].split('#')

    if len(messages_list[0]) > 1:
        for j in messages_list:
            if j[0] == '阿短':
                with st.chat_message('🌞'):
                    st.text(j[0] + ':' + j[1])
            elif j[0] == '编程猫':
                with st.chat_message('🍥'):
                    st.text(j[0] + ':' + j[1])
    # 新增留言
    name = st.selectbox('我是……', ['阿短', '编程猫'])
    new_message = st.text_input('想要说的话……')
    if st.button('留言'):
        with open('leave_messages.txt', 'a', encoding='utf-8') as f:
            message = ''
            message += name + '#' + new_message + '\n'
            f.write(message)

def page_5():
    # 猜一猜
    st.write(':cake:你知道我的生日是几月几日吗？:cake')
    birthday = st.text_input('输入样例:0123(即1月23日)')
    if birthday == '0810':
        st.balloons()
        st.write('你猜对了')


if page == '我的兴趣推荐':
    page_1()
elif page == '我的图片处理工具':
    page_2()
elif page == '我的智慧词典':
    page_3()
elif page == '我的留言区':
    page_4()
elif page == '猜一猜':
    page_5()


