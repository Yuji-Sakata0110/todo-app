export interface AuthInterface {
  email: string;
  password: string;
}

export interface getJwtAccessTokenResponseInterface {
  access: string;
  refresh: string;
}
export interface LoginResponseInterface {
  login_status: boolean;
}

export interface AuthHeaderInterface {
  headers: {
    Authorization: string;
    "Content-Type": string;
  };
}
