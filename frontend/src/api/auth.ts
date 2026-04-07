import api from "./client";
import {
  type LoginRequest,
  type RegisterRequest,
  type TokenResponse,
} from "./types";

export async function login(data: LoginRequest) {
  const response = await api.post("token/", data);
  return response.data;
}

export async function register(data: RegisterRequest): Promise<TokenResponse> {
  const response = await api.post("users/", data);
  return response.data;
}

export async function authService(type: "login" | "register", data: any) {
  return type === "login" ? login(data) : register(data);
}
