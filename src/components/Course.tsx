
export default function Course({name}: {name: string}) {
    return <div className="w-48 h-32 flex align-items-center justify-center rounded shadow border border-2">
        <p>{name}</p>
    </div>;
  }