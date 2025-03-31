import Image from "next/image";
import Link from "next/link";

export default function Home() {
  return (
    <div>
      <h1>Music Dating App</h1>
      <h2>Discover New Music Tailored to Your Taste</h2>
      <div>
        <Link>
          <button href="/login">Log In</button>
        </Link>
        <Link>
          <button href="/signup">Sign Up</button>
        </Link>
      </div>
    </div>
  );
}
