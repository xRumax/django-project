interface TextProps {
  content: string;
  size?: "small" | "large";
}

export const Text = ({ content }: TextProps) => {
  return <p>{content}</p>;
};
