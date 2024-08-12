from pydub import AudioSegment
 
if __name__ == '__main__':
    mp3_file_path = r"C:\Program Files (x86)\NBroadcast\Release\Music\试音碟-加州旅馆333.mp3"
    # wav_file_path = r"E:\20240326\output\airuhuo_T4_w\airuhuo.wav"
 
    # 加载 MP3 文件
    audio = AudioSegment.from_mp3(mp3_file_path)
 
    # 导出为 WAV 格式
    # audio.export(wav_file_path, format='wav')
 
    frame_rate = audio.frame_rate
    print("帧率（采样率）:", frame_rate, "Hz")
 
    # 获取总时长（以毫秒为单位）
    # duration_ms = len(audio)
    # print("总时长:", duration_ms, "毫秒")
 
    # 如果需要以秒为单位的时长，可以进行转换
    #duration_seconds = duration_ms / 1000.0
    #print("总时长:", duration_seconds, "秒")