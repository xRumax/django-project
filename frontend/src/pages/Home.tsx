import { Text } from "../components/atoms/Text";
import { Button } from "../components/atoms/Button";

export default function Home() {
  function handleClick() {
    console.log("Klik!");
  }
  return (
    <>
      <div className="text-container">
        <Text content="Halo halo" />
      </div>
      <div className="button-space">
        <Button label="Potwierdź" type="submit" onClick={handleClick} />
      </div>
    </>
  );
}
