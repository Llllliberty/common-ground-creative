import AgentWorkspace from './agent-workspace';

export default async function AgentPage({
  searchParams,
}: {
  searchParams: Promise<{ stage?: string }>;
}) {
  const { stage } = await searchParams;
  return <AgentWorkspace initialStage={stage === 'summary' ? 'summary' : 'upload'} />;
}
