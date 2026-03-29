export interface ActivityLink {
  label: string;
  url: string;
}

export interface Activity {
  time: string;
  icon: string;
  title: string;
  description: string;
  tip: string;
  links: ActivityLink[];
}

export interface Day {
  day: number;
  date: string;
  title: string;
  emoji: string;
  location: string;
  hero_image: string;
  map_lat: string;
  map_lng: string;
  map_gmaps: string;
  activities: Activity[];
}
