import { Md5 } from 'ts-md5'

export function hashMd5(string: string): string {
  const md5 = new Md5()
  md5.appendStr(string)
  return String(md5.end())
}

// admin: {
//     login: "secrAd56",
//     password: "gveih5yh.5"
// }
