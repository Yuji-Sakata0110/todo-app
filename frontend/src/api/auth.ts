import axios, { Axios, AxiosError, AxiosResponse } from "axios";
import {
  AuthInterface,
  LoginResponseInterface,
  AuthHeaderInterface,
  getJwtAccessTokenResponseInterface,
} from "../interfaces/auth";
import { request } from "http";

export const checkAccessToken = (): boolean => {
  return false;
};

export const getJwtAccessToken = async (): Promise<void> => {
  try {
    await axios
      .post<getJwtAccessTokenResponseInterface>(
        "http://localhost:8000/api/auth/token/",
        user
      )
      .then((res) => {
        localStorage.setItem("Token", res.data.access);
      });
  } catch (error) {
    console.error(error);
  }
};

// export const getJwtRefreshToken = async (): Promise<void> => {
//   try {
//     await axios
//       .post<SignInResponseInterface>(
//         "http://localhost:8000/api/token/",
//         user,
//         reqHeader
//       )
//       .then((res) => {
//         localStorage.setItem("Token", res.data.access_token);
//       });
//   } catch (error) {
//     // axios エラーかチェックする。
//     if (axios.isAxiosError(error)) {
//       const axiosError: AxiosError = error;
//       // 401の場合、Tokenを新規で作成し、Localstrageに保存する。
//       if (axiosError.response?.status === 401) {
//         console.log("Request new JWT Token.");
//       }
//     }
//     // 不明なエラーをハンドリングする。
//     else {
//       throw new Error(`Unknown Error is occured. ${error}`);
//     }
//   }
// };

// export const signUp = async (): Promise<void> => {
//   try {
//     await axios
//       .post<SignInResponseInterface>(
//         "http://localhost:8000/api/auth/signup/",
//         user
//       )
//       .then((res) => localStorage.setItem("Token", res.data.access_token));
//   } catch (error) {
//     console.error(error);
//   }
// };

export const login = async (): Promise<any> => {
  try {
    const res: AxiosResponse<LoginResponseInterface> =
      await axios.post<LoginResponseInterface>(
        "http://localhost:8000/api/auth/login/",
        user
      );
    return res.data.login_status;
  } catch (error) {
    // // axios エラーかチェックする。
    if (axios.isAxiosError(error)) {
      const axiosError: AxiosError = error;
      // Token認証が失敗した場合、Tokenを再発行し、再認証を行う。リトライ回数を最大3回とする。
      if (axiosError.response?.status === 401) {
        throw `axios error: ${error}`;
      }
    }
    // 不明なエラーをハンドリングする。
    else {
      throw `Unknown Error is occured. ${error}`;
    }
  }
};

// export const signOut = async (): Promise<void> => {
//   // logout
//   axios.post;
// };

const user: AuthInterface = {
  email: "sample2@gmail.com",
  password: "aaa",
};

const jwtToken: string | null = localStorage.getItem("Token");
// const jwtToken: string =
//   "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjk5NzYwMTY5LCJpYXQiOjE2OTk3NTkyNjksImp0aSI6IjcwZGQ5Y2Y1Y2Y5YTRkM2M5YzU4ZDQzYjA4MDVmZTQ1IiwidXNlcl9pZCI6ImNlNjc5NTQxLWFiYjYtNGY4ZC04YmNiLTMxYWU1MGFiNTc3NSJ9.1WAFbZrXe3zUNfLCB9iFe3w8KFpGmltxhvaJNDH7MvI";

export const reqHeader: AuthHeaderInterface = {
  headers: {
    Authorization: `Bearer ${jwtToken}`,
    "Content-Type": "application/json",
  },
};
