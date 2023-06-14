from concurrent.futures import thread
import sys
from win10toast import ToastNotifier
import webbrowser
import functools
import operator
import os
import cv2
import time
import joblib
import numpy as np
from keras.layers import Input, LSTM, Dense
from keras.models import Model, load_model
from edamam_nutrition_api_access import info
import extract_features


from fpdf import FPDF

import config
import PIL.Image, PIL.ImageTk
from tkinter.filedialog import askopenfilename
# import imutils

try:
    import tkinter as tk
except ImportError:
    import tkinter as tk


import Design_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Toplevel1 (root)
    Design_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_Toplevel1(root, *args, **kwargs)' .'''
    global w, w_win, root
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    Design_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:

    def showvideocaption(self,a,b):
        

        if(self.knob  == 0):
            self.toaster.show_toast("Upload Video First",duration=5,threaded=True,msg="Video Caption Project")
            return
            
        for widget in b.winfo_children():
            widget.destroy()
            break
        self.canvas = tk.Canvas(b, width = self.vid.width + 200, height = self.vid.height + 200)
        self.canvas.pack()
        self.turner = 1
        self.checkflag = True
        a.load_inference_models()
        result = self.filename.split('/')[-1]
        self.filer = result
        # result = result[0]
        
        
        self.toaster.show_toast("Generating Video Captions ",duration=5,threaded=True,msg="Video Caption Project")
        
        while True:
            print('.........................\nGenerating Caption:\n')
            start = time.time()
            video_caption, file = a.test(self.filer)
            end = time.time()
            self.sentence = ''
            print(self.sentence)
            for text in video_caption.split():
                self.sentence = self.sentence + ' ' + text
                print('\n.........................\n')
                print(self.sentence)
                
            print('\n.........................\n')
            print('It took {:.2f} seconds to generate caption'.format(end-start))
            break

    def getnutrients(self,a,b):
        for widget in a.winfo_children():
            widget.destroy()
            break
        self.turner = 0

        listbox = tk.Listbox(a, height = 13, 
                  width = 35, 
                  bg = "black",
                  activestyle = 'dotbox', 
                  font = "Helvetica",
                  fg = "white")
        count = 1

        
        try:
            self.text = info(self.sentence)
            self.mpdf = True
            self.text = self.text[0].get('food').get('nutrients')
            for key,value in self.text.items():
                pair = key + "  " + str(value)
                listbox.insert(count,pair)
                count +=1
        except:
            print("No nutrient Info")
            self.mpdf = False
            listbox.insert(count,"No Such Information Available")
            count += 1
        
        
        self.toaster.show_toast("Nutrients Are Generated",duration=5,threaded=True,msg="Video Caption Project")

        listbox.pack()

    def caption(self,home):
        for widget in home.winfo_children():
            widget.destroy()
            break
        # self.canvas.destroy()
        
        
        self.toaster.show_toast("Captions Generated",duration=5,threaded=True,msg="Video Caption Project")

        self.turner = 0
        text_widget = tk.Text(home,
                           width=40, height=10)
        text_widget.insert(tk.END,self.sentence)
        text_widget.pack()

    
    def upload(self,a):
        self.knob = 1
        self.turner = 0
        if(len(self.sentence) > 0):
            self.sentence = ''
        for widget in a.winfo_children():
            widget.destroy()
            break
            
        
        self.filename = askopenfilename()
        split_tup = os.path.splitext(self.filename)
       
        if(len(self.filename) <= 0 ):
            self.toaster.show_toast("No File Selected",duration=5,threaded=True,msg="Video Caption Project")
            return

        elif(split_tup[1] != '.avi'):
            self.toaster.show_toast("File Format Not Supported. Please Use .avi",duration=5,threaded=True,msg="Video Caption Project")
            return
        else:
            self.toaster.show_toast("File Uploaded Succesfully",duration=5,threaded=True,msg="Video Caption Project")

        self.video_source = self.filename
        self.filer = self.video_source
        self.vid = MyVideoCapture(self.video_source)
        
        

        self.canvas = tk.Canvas(a, width = self.vid.width + 200, height = self.vid.height + 200)
        self.canvas.pack()
        
        self.turner = 1
            
        
        # if(self.vid):

        #     self.vid = MyVideoCapture(self.video_source)
    def makepdf(self):
        pdf = FPDF()
 
        # Add a page
        pdf.add_page()
        
        # set style and size of font
        # that you want in the pdf
        
        pdf.set_font("Arial", size = 15)
        
        # create a cell
        pdf.cell(100, 10, txt = self.sentence,
                ln = 2, align = 'C')
        
        # add another cell
        if(self.mpdf):
            pdf.cell(200, 10, txt = str(self.text),
                ln = 2, align = 'C')
        else:
            pdf.cell(100, 10, txt = "No Nutrient Information Is Available",
                ln = 2, align = 'C')
        # print("Here I am Now")
        self.toaster.show_toast("Pdf Generated Succesfully",duration=5,threaded=True,msg="Video Caption Project")
        # save the pdf with name .pdf
        pdf.output("Nutrion.pdf")  

    @staticmethod
    def showLink(self):
        webbrowser.open('https://www.youtube.com/watch?v=WnMQ8HlmeXc')
    
    def showsupport(self,a,b):
        for widget in a.winfo_children():
            widget.destroy()
            break
        self.turner = 0
        text_widget = tk.Text(a,width=70, height=15)
        text_widget.insert(tk.END," 1. First Upload Video from dataset trained in local-disk \n \n 2. Generate Caption from uploaded video \n \n 3. Show caption of uploaded video \n \n 4. Generate nutrition information of ingredients used in video \n \n 5. Downlooad report in PDF Form \n\n")
        # hyperlink= HyperlinkManager(text)

        text_widget.insert(tk.END, " 6. For more details click to see 'youtube video' ", ("link", "href"))
        text_widget.tag_bind('link', '<Button-1>', self.showLink)
        text_widget.pack()


    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        
        self.toaster = ToastNotifier()
        self.knob = 0
        self.config = config
        
        self.sentence = ''
        self.uploader = 0
        self.filename = ''
        self.filer = ''
        self.text = ''
        self.mpdf = True

        """We are Making instance of our video Class here"""
        
        self.video_source = "C:\\Users\\Snekha\\Desktop\\video-captioning\\vid.avi"


        # if(self.uploader == 1):

        self.checkflag = False
        self.vid = MyVideoCapture(self.video_source)
        
        

        self.canvas = ''

        self.turner = 1
       
        
        
        """The EndGame"""

        top.geometry("864x508+282+95")
        top.minsize(120, 1)
        top.maxsize(1370, 749)
        top.resizable(1,  1)
        top.title("Cooking based Video-Captioning Through Deep Learning")
        top.configure(background="#ffffff")
        top.configure(height="10")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.menubar = tk.Frame(top)
        self.menubar.place(relx=-0.001, rely=0.0, relheight=1.028, relwidth=0.191)
        self.menubar.configure(relief='groove')
        self.menubar.configure(borderwidth="2")
        self.menubar.configure(relief="groove")
        self.menubar.configure(background="#1b1b1b")
        self.menubar.configure(highlightbackground="#d9d9d9")
        self.menubar.configure(highlightcolor="black")



        """Start of Home Frame"""

        self.home = tk.Frame(top,highlightbackground = "black",highlightthickness=2)
        # self.home.place(relx=0.189, rely=0.114, relheight=0.915, relwidth=0.816)
        self.home.place(relx=0.189, rely=0.114, relheight=0.915, relwidth=0.816)
        self.home.configure(relief='groove')
        self.home.configure(borderwidth="5")
        self.home.configure(relief="groove")
        self.home.configure(background="#ffffff")
        self.home.configure(highlightbackground="black")
        self.home.configure(highlightcolor="black")


        """End of Home Frame"""

        self.dwnldpdf = tk.Button(self.menubar,command=lambda:self.makepdf())
        self.dwnldpdf.place(relx=0.012, rely=0.53, height=64, width=157)
        self.dwnldpdf.configure(activebackground="#ececec")
        self.dwnldpdf.configure(activeforeground="#000000")
        self.dwnldpdf.configure(background="#1b1b1b")
        self.dwnldpdf.configure(disabledforeground="#a3a3a3")
        self.dwnldpdf.configure(foreground="#ffffff")
        self.dwnldpdf.configure(highlightbackground="#d9d9d9")
        self.dwnldpdf.configure(highlightcolor="black")
        self.dwnldpdf.configure(pady="0")
        self.dwnldpdf.configure(text='''Downlad PDF''')

        
       
            
        self.Uploadvideo = tk.Button(self.menubar, text ='Choose File ',command=lambda:self.upload(self.home))
        self.Uploadvideo.place(relx=0.012, rely=0.13, height=64, width=157)
        self.Uploadvideo.configure(activebackground="#ececec")
        self.Uploadvideo.configure(activeforeground="#000000")
        self.Uploadvideo.configure(background="#1b1b1b")
        self.Uploadvideo.configure(disabledforeground="#a3a3a3")
        self.Uploadvideo.configure(foreground="#ffffff")
        self.Uploadvideo.configure(highlightbackground="#d9d9d9")
        self.Uploadvideo.configure(highlightcolor="black")
        self.Uploadvideo.configure(pady="0")
        self.Uploadvideo.configure(text='''Upload Video''')

       

        self.generatecaption = tk.Button(self.menubar,command=lambda:self.showvideocaption(self.vid,self.home))
        self.generatecaption.place(relx=0.012, rely=0.23, height=64, width=157)
        self.generatecaption.configure(activebackground="#ececec")
        self.generatecaption.configure(activeforeground="#000000")
        self.generatecaption.configure(background="#1b1b1b")
        self.generatecaption.configure(disabledforeground="#a3a3a3")
        self.generatecaption.configure(foreground="#ffffff")
        self.generatecaption.configure(highlightbackground="#d9d9d9")
        self.generatecaption.configure(highlightcolor="black")
        self.generatecaption.configure(pady="0")
        self.generatecaption.configure(text='''Generate Caption''')

        self.showcaption = tk.Button(self.menubar,command=lambda:self.caption(self.home))
        self.showcaption.place(relx=0.012, rely=0.33, height=64, width=157)
        self.showcaption.configure(activebackground="#ececec")
        self.showcaption.configure(activeforeground="#000000")
        self.showcaption.configure(background="#1b1b1b")
        self.showcaption.configure(disabledforeground="#a3a3a3")
        self.showcaption.configure(foreground="#ffffff")
        self.showcaption.configure(highlightbackground="#d9d9d9")
        self.showcaption.configure(highlightcolor="black")
        self.showcaption.configure(pady="0")
        self.showcaption.configure(text='''Show Caption''')

        self.Nutrioninfo = tk.Button(self.menubar,command=lambda:self.getnutrients(self.home,self.sentence))
        self.Nutrioninfo.place(relx=0.012, rely=0.43, height=64, width=157)
        self.Nutrioninfo.configure(activebackground="#ececec")
        self.Nutrioninfo.configure(activeforeground="#000000")
        self.Nutrioninfo.configure(background="#1b1b1b")
        self.Nutrioninfo.configure(disabledforeground="#a3a3a3")
        self.Nutrioninfo.configure(foreground="#ffffff")
        self.Nutrioninfo.configure(highlightbackground="#d9d9d9")
        self.Nutrioninfo.configure(highlightcolor="black")
        self.Nutrioninfo.configure(pady="0")
        self.Nutrioninfo.configure(text='''Nutrition Info''')

        self.videolabel = tk.Label(self.menubar)
        self.videolabel.place(relx=0.03, rely=0.006, height=63, width=155)
        self.videolabel.configure(activebackground="#000000")
        self.videolabel.configure(activeforeground="white")
        self.videolabel.configure(activeforeground="#ffffff")
        self.videolabel.configure(background="#000000")
        self.videolabel.configure(disabledforeground="#a3a3a3")
        self.videolabel.configure(font="-family {Yu Gothic UI Semibold} -size 10 -weight bold -slant italic")
        self.videolabel.configure(foreground="#ffffff")
        self.videolabel.configure(highlightbackground="#d9d9d9")
        self.videolabel.configure(highlightcolor="black")
        self.videolabel.configure(text='''Home''')

        self.support = tk.Button(self.menubar,command=lambda:self.showsupport(self.home,self.sentence))
        self.support.place(relx=0.0, rely=0.891, height=50, width=166)
        self.support.configure(activebackground="#f9f9f9")
        self.support.configure(activeforeground="black")
        self.support.configure(background="#000000")
        self.support.configure(disabledforeground="#a3a3a3")
        self.support.configure(foreground="#ffffff")
        self.support.configure(highlightbackground="#d9d9d9")
        self.support.configure(highlightcolor="black")
        self.support.configure(text='''Support''')


        self.menubar = tk.Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

        self.defination = tk.Label(top)
        self.defination.place(relx=0.19, rely=0.0, height=61, width=704)
        self.defination.configure(activebackground="#f9f9f9")
        self.defination.configure(activeforeground="black")
        self.defination.configure(background="#1b1b1b")
        self.defination.configure(disabledforeground="#a3a3a3")
        self.defination.configure(foreground="#ffffff")
        self.defination.configure(highlightbackground="#d9d9d9")
        self.defination.configure(highlightcolor="black")
        self.defination.configure(font="-family {Yu Gothic UI Semibold} -size 16 -weight bold -slant italic")
        self.defination.configure(text='''Cooking based Video-Captioning''')

        # self.home = tk.Frame(top)
        # self.home.place(relx=0.189, rely=0.114, relheight=0.915, relwidth=0.816)
        # self.home.configure(relief='groove')
        # self.home.configure(borderwidth="2")
        # self.home.configure(relief="groove")
        # self.home.configure(background="#ffffff")
        # self.home.configure(highlightbackground="#d9d9d9")
        # self.home.configure(highlightcolor="black")

       
        

        self.canvas = tk.Canvas(self.home, width = self.vid.width + 100, height = self.vid.height + 100)
        # self.canvas = tk.Canvas(self.home, width = 700, height = 700,background='white')
        self.canvas.pack()
        self.delay = 25
        self.update()
    
    

    def update(self):
        if(self.turner == 1):

            # Get a frame from the video source
           
            
            ret, frame = self.vid.get_frame(self.sentence)
           
    
            if ret:
                self.photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
                self.canvas.create_image(0, 0, image = self.photo, anchor = tk.NW)
    
        self.home.after(self.delay, self.update)

class MyVideoCapture:

        
    def __init__(self, video_source):
        # Open the video source
       
        self.vid = cv2.VideoCapture(video_source)
        
       #  if not self.vid.isOpened():
       #      raise ValueError("Unable to open video source", video_source)

        # Get video source width and height
        self.width = self.vid.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height = self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT)

        
        self.checkmate = True
        
        ##############################################
        
        self.latent_dim = config.latent_dim
        self.num_encoder_tokens = config.num_encoder_tokens
        self.num_decoder_tokens = config.num_decoder_tokens
        self.time_steps_encoder = config.time_steps_encoder
        self.max_probability = config.max_probability

        # models
        self.encoder_model = None
        self.decoder_model = None
        self.inf_encoder_model = None
        self.inf_decoder_model = None
        self.save_model_path = config.save_model_path
        self.test_path = config.test_path
        self.search_type = config.search_type
        self.tokenizer = None
        self.num = 3

    def rescale_frame(frame, percent=75):
        width = int(frame.shape[1] * percent/ 100)
        height = int(frame.shape[0] * percent/ 100)
        dim = (width, height)
        return cv2.resize(frame, dim, interpolation =cv2.INTER_AREA)


    def get_frame(self,sentence):
        
        
        if(sentence and self.checkmate):
             _ = self.vid.set(cv2.CAP_PROP_POS_FRAMES, 0)
             self.checkmate = False
        b = int(self.vid.get(cv2.CAP_PROP_FRAME_COUNT))
        if(self.vid.get(cv2.CAP_PROP_POS_FRAMES) == b):
            _ = self.vid.set(cv2.CAP_PROP_POS_FRAMES, 0)
            

        if self.vid.isOpened():
            ret, frame = self.vid.read()
            if ret:
                # Return a boolean success flag and the current frame converted to BGR
                
                # s = cv2.putText(frame, sentence, (100, 270), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255),2, cv2.LINE_4)
                
                wd = 0
                hg = int(self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT)//2)
                # f_width = int(self.vid.get(cv2.CAP_PROP_FRAME_WIDTH)) + 100
                # f_height = int(self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT)) + 100
                # frame = cv2.resize(frame,(f_width,f_height))
              
                s = cv2.putText(frame, sentence, (wd,hg),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,0,0),1)
                s = cv2.cvtColor(s, cv2.COLOR_BGR2RGB)
                return (ret, s)
            else:
                return (ret, None)
        else:
            return (None,None)
        

    # Release the video source when the object is destroyed
    def __del__(self):
        if self.vid.isOpened():
            self.vid.release()

    
   
    def load_inference_models(self):
       # load tokenizer

       with open(os.path.join(self.save_model_path, 'tokenizer' + str(self.num_decoder_tokens)), 'rb') as file:
           self.tokenizer = joblib.load(file)

       # inference encoder model
       self.inf_encoder_model = load_model(os.path.join(self.save_model_path, 'encoder_model.h5'))

       # inference decoder model
       decoder_inputs = Input(shape=(None, self.num_decoder_tokens))
       decoder_dense = Dense(self.num_decoder_tokens, activation='softmax')
       decoder_lstm = LSTM(self.latent_dim, return_sequences=True, return_state=True)
       decoder_state_input_h = Input(shape=(self.latent_dim,))
       decoder_state_input_c = Input(shape=(self.latent_dim,))
       decoder_states_inputs = [decoder_state_input_h, decoder_state_input_c]
       decoder_outputs, state_h, state_c = decoder_lstm(decoder_inputs, initial_state=decoder_states_inputs)
       decoder_states = [state_h, state_c]
       decoder_outputs = decoder_dense(decoder_outputs)
       print("The outputs are : ",decoder_outputs)
       self.inf_decoder_model = Model(
           [decoder_inputs] + decoder_states_inputs,
           [decoder_outputs] + decoder_states)
       self.inf_decoder_model.load_weights(os.path.join(self.save_model_path, 'decoder_model_weights.h5'))

    def greedy_search(self, f):
       """

       :param f: the loaded numpy array after creating videos to frames and extracting features
       :return: the final sentence which has been predicted greedily
       """
       print("The greededfdfsdfkds")
       inv_map = self.index_to_word()
       states_value = self.inf_encoder_model.predict(f.reshape(-1, 80, 4096))
       target_seq = np.zeros((1, 1, 1500))
       final_sentence = ''
       target_seq[0, 0, self.tokenizer.word_index['bos']] = 1
       for i in range(15):
           output_tokens, h, c = self.inf_decoder_model.predict([target_seq] + states_value)
           states_value = [h, c]
           output_tokens = output_tokens.reshape(self.num_decoder_tokens)
           y_hat = np.argmax(output_tokens)
           if y_hat == 0:
               continue
           if inv_map[y_hat] is None:
               break
           if inv_map[y_hat] == 'eos':
               break
           else:
               final_sentence = final_sentence + inv_map[y_hat] + ' '
               target_seq = np.zeros((1, 1, 1500))
               target_seq[0, 0, y_hat] = 1
       return final_sentence

    def decode_sequence2bs(self, input_seq):
       states_value = self.inf_encoder_model.predict(input_seq)
       target_seq = np.zeros((1, 1, self.num_decoder_tokens))
       target_seq[0, 0, self.tokenizer.word_index['bos']] = 1
       self.beam_search(target_seq, states_value, [], [], 0)
       return decode_seq

    def beam_search(self, target_seq, states_value, prob, path, lens):
       """

       :param target_seq: the array that is fed into the model to predict the next word
       :param states_value: previous state that is fed into the lstm cell
       :param prob: probability of predicting a word
       :param path: list of words from each sentence
       :param lens: number of words
       :return: final sentence
       """
       global decode_seq
       node = 2
       output_tokens, h, c = self.inf_decoder_model.predict(
           [target_seq] + states_value)
       output_tokens = output_tokens.reshape(self.num_decoder_tokens)
       sampled_token_index = output_tokens.argsort()[-node:][::-1]
       states_value = [h, c]
       for i in range(node):
           if sampled_token_index[i] == 0:
               sampled_char = ''
           else:
               sampled_char = list(self.tokenizer.word_index.keys())[
                   list(self.tokenizer.word_index.values()).index(sampled_token_index[i])]
           MAX_LEN = 12
           if sampled_char != 'eos' and lens <= MAX_LEN:
               p = output_tokens[sampled_token_index[i]]
               if sampled_char == '':
                   p = 1
               prob_new = list(prob)
               prob_new.append(p)
               path_new = list(path)
               path_new.append(sampled_char)
               target_seq = np.zeros((1, 1, self.num_decoder_tokens))
               target_seq[0, 0, sampled_token_index[i]] = 1.
               self.beam_search(target_seq, states_value, prob_new, path_new, lens + 1)
           else:
               p = output_tokens[sampled_token_index[i]]
               prob_new = list(prob)
               prob_new.append(p)
               p = functools.reduce(operator.mul, prob_new, 1)
               if p > self.max_probability:
                   decode_seq = path
                   self.max_probability = p

    def decoded_sentence_tuning(self, decoded_sentence):
       # tuning sentence
       decode_str = []
       filter_string = ['bos', 'eos']
       uni_gram = {}
       last_string = ""
       for idx2, c in enumerate(decoded_sentence):
           if c in uni_gram:
               uni_gram[c] += 1
           else:
               uni_gram[c] = 1
           if last_string == c and idx2 > 0:
               continue
           if c in filter_string:
               continue
           if len(c) > 0:
               decode_str.append(c)
           if idx2 > 0:
               last_string = c
       return decode_str

    def index_to_word(self):
       # inverts word tokenizer
       index_to_word = {value: key for key, value in self.tokenizer.word_index.items()}
       return index_to_word

    def get_test_data(self,filer):
       
       # loads the features array
    #    file_list = os.listdir(os.path.join(self.test_path, 'video'))
       
       # with open(os.path.join(self.test_path, 'testing.txt')) as testing_file:
           # lines = testing_file.readlines()
       # file_name = lines[self.num].strip()
    #    file_name = file_list[self.num]
       path = os.path.join(self.test_path, 'feat', filer + '.npy')
       if os.path.exists(path):
           f = np.load(path)
       else:
           model = extract_features.model_cnn_load()
           
          
           f = extract_features.extract_features(filer, model)
           
    #    if self.num < len(file_list):
    #        self.num += 1
    #    else:
    #        self.num = 0
       return f, filer

    def test(self,filer):
       X_test, filename = self.get_test_data(filer)
       # generate inference test outputs
       if self.search_type == 'greedy':
           sentence_predicted = self.greedy_search(X_test.reshape((-1, 80, 4096)))
       else:
           sentence_predicted = ''
           decoded_sentence = self.decode_sequence2bs(X_test.reshape((-1, 80, 4096)))
           decode_str = self.decoded_sentence_tuning(decoded_sentence)
           for d in decode_str:
               sentence_predicted = sentence_predicted + d + ' '
       # re-init max prob
       self.max_probability = -1
       return sentence_predicted, filename

    def main(self, filename, caption):
        
       """

       :param filename: the video to load
       :param caption: final caption
       :return:
       """
       # 1. Initialize reading video object
       cap1 = cv2.VideoCapture(os.path.join(self.test_path, 'video', filename))
       cap2 = cv2.VideoCapture(os.path.join(self.test_path, 'video', filename))
       caption = '[' + ' '.join(caption.split()[1:]) + ']'
       # 2. Cycle through pictures
       while cap1.isOpened():
           ret, frame = cap2.read()
           ret2, frame2 = cap1.read()
           if ret:
               imS = cv2.resize(frame, (480, 300))
               cv2.putText(imS, caption, (100, 270), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0),
                           2, cv2.LINE_4)
               cv2.imshow("VIDEO CAPTIONING", imS)
           if ret2:
               imS = cv2.resize(frame, (480, 300))
               cv2.imshow("ORIGINAL", imS)
           else:
               break

           # Quit playing
           key = cv2.waitKey(25)
           if key == 27:  # Button esc
               break

       # 3. Free resources
       cap1.release()
       cap2.release()
       cv2.destroyAllWindows()


if __name__ == '__main__':
    vp_start_gui()





