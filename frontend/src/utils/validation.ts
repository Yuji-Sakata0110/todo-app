import { validationRuleInterface } from "./../interfaces/validation";

const validationRules: validationRuleInterface = { isEmpty: /^\s*$/ };

export const validation = (inputText: string): boolean => {
  if (validationRules.isEmpty.test(inputText)) {
    console.error("ValidationError: 空白でtodoを追加することができません。");
    return true;
  }
  return false;
};
