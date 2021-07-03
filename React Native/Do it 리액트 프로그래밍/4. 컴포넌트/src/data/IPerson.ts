// 모바일 앱은 보통 JSON 데이터를 원격지 API 서버에서 수신하여 화면에 출력하는 방식으로 동작한다.
// 다음과 같은 형식으로 서버에서 데이터를 수신한다.

type IPerson = {
  id: string;
  createdDate: Date;
  modifiedDate: Date;
  name: string;
  email: string;
  avatar: string;
  image: string;
  comments: string;
  counts: {
    comment: number;
    retweet: number;
    heart: number;
  };
};
export type {IPerson};
