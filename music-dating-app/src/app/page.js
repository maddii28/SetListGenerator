import Image from "next/image";
import Link from "next/link";

export default function Home() {
  return (
    <div>
      <h1>Music Dating App</h1>
      <h2>Discover New Music Tailored to Your Taste</h2>
      <div>
        <Link href="/login">
          <button>Log In</button>
        </Link>
        <Link href="/signup">
          <button>Sign Up</button>
        </Link>
      </div>
    </div>
  );
}
