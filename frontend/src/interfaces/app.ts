import { Dispatch, SetStateAction } from "react";

export interface LoginContextInterface {
  isLogin: boolean;
  setIsLogin: Dispatch<SetStateAction<boolean>>;
}
