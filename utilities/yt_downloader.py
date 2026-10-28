import os
import yt_dlp

DEFAULT_URL = "https://www.youtube.com/watch?v=DtJ6Q_m8kVg"

def progress_hook(d):
    """다운로드 진행 상태를 텍스트로 예쁘게 출력해주는 훅"""
    if d['status'] == 'downloading':
        percent = d.get('_percent_str', '0.0%').strip()
        speed = d.get('_speed_str', 'N/A').strip()
        eta = d.get('_eta_str', 'N/A').strip()
        print(f"📥 다운로드 중... [{percent}] (속도: {speed}, 남은 시간: {eta})", end='\r')
    elif d['status'] == 'finished':
        print("\n✨ 다운로드 완료! 파일 후처리(변환/합병) 중...")

def download_youtube_media(url, mode='audio'):
    output_dir = "downloads"
    os.makedirs(output_dir, exist_ok=True)

    ydl_opts = {
        'progress_hooks': [progress_hook],
        'outtmpl': os.path.join(output_dir, '%(title)s.%(ext)s'),
        'noplaylist': True, # ★ 핵심: 플레이리스트나 믹스 링크여도 딱 1개의 영상만 다운로드함!
    }

    if mode == 'audio':
        print("🎵 [오디오 모드] 최고 음질 MP3 추출을 시작합니다...")
        ydl_opts.update({
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        })
    else:
        print("🎬 [비디오 모드] 최고 화질 MP4 다운로드를 시작합니다...")
        ydl_opts.update({
            'format': 'bestvideo+bestaudio/best',
        })

    print(f"🔗 대상 주소: {url}")
    print("⏳ 유튜브 서버에서 정보를 분석 중입니다. 잠시만 기다려주세요...\n")

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print(f"\n🎉 작업 완료! '{output_dir}' 폴더를 확인하세요.")
    except Exception as e:
        print(f"\n❌ 오류 발생: {e}")

if __name__ == '__main__':
    print("=" * 50)
    print("   유튜브 미디어 다운로더 (yt-dlp)")
    print("=" * 50)
    
    user_input = input("🔗 유튜브 URL을 입력하세요 (그냥 엔터 치면 기본 URL 사용): ").strip()
    target_url = user_input if user_input else DEFAULT_URL
    
    print("\n추출 모드를 선택하세요:")
    print(" 1 : 오디오 (MP3 추출) [기본값]")
    print(" 2 : 비디오 (MP4 영상 다운로드)")
    choice = input("선택 (1 또는 2, 그냥 엔터 치면 1): ").strip()
    
    mode = 'video' if choice == '2' else 'audio'
    
    download_youtube_media(target_url, mode)