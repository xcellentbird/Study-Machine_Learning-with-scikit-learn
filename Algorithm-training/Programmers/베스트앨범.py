def solution(genres, plays):
    answer = []
    playlist = {}
    for song, genre, play  in zip(range(len(plays)), genres, plays):
        if genre not in playlist:
            playlist[genre] = {}
        playlist[genre][song] = play
    
    best_genres = sorted(list(playlist), reverse=True, key=lambda x: sum(playlist[x].values()))
    
    for genre in best_genres:
        best_songs = sorted(list(playlist[genre]), reverse=True, key = lambda x: playlist[genre][x])
        answer+=best_songs[:2]
    
    return answer
