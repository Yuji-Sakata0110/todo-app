import { Dispatch, SetStateAction } from "react";

export interface PropsInterface {
  setIsLogin: Dispatch<SetStateAction<boolean>>;
}

export interface PropsNavigationInterface {
  isLogin: boolean;
  setIsLogin: Dispatch<SetStateAction<boolean>>;
}
