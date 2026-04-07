import { Text } from "../components/atoms/Text";
import AuthForm from "../components/molecules/AuthForm";
export default function Login() {
  return (
    <>
      <div className="flex  justify-center">
        <Text content="Login page" />
        <div>
          <AuthForm type="login" />
        </div>
      </div>
    </>
  );
}
