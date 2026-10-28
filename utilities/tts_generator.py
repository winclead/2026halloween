import os
from gtts import gTTS

def generate_voice(text, filename="narration.mp3"):
    """
    텍스트를 입력받아 음성 MP3 파일로 변환해주는 유틸리티 함수
    """
    output_dir = "downloads"
    os.makedirs(output_dir, exist_ok=True)
    
    file_path = os.path.join(output_dir, filename)
    
    print(f"🎙️ 음성 생성 중: '{text}'")
    
    # 구글 TTS를 이용해 한국어 음성 생성 (slow=False는 정상 속도)
    tts = gTTS(text=text, lang='ko', slow=False)
    tts.save(file_path)
    
    print(f"🎉 음성 파일 저장 완료: {file_path}")
    return file_path

if __name__ == '__main__':
    print("=" * 50)
    print("   서바이벌 나레이션 TTS 생성기 (gTTS)")
    print("=" * 50)
    
    user_text = input("입력할 대사를 적어주세요 (예: 메인 피의자가 탈락했습니다.): ").strip()
    file_name = input("저장할 파일명 입력 (기본값: narration.mp3): ").strip()
    
    if not file_name:
        file_name = "narration.mp3"
    if not file_name.endswith(".mp3"):
        file_name += ".mp3"
        
    if user_text:
        generate_voice(user_text, file_name)
    else:
        print("❌ 텍스트가 입력되지 않았습니다.")