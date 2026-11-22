import {Composition} from 'remotion';
import {Main} from './Main';
import data from './data.json';
export const Root = () => (
  <Composition id="Edit" component={Main} width={1080} height={1920} fps={(data as any).fps} durationInFrames={(data as any).total} />
);
