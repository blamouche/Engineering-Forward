# Building a Home Robot With Zero Robot Data
**Source**: https://itcanthink.substack.com/p/building-a-home-robot-with-zero-robot
**Date**: 2026-03-12
**Author**: Chris Paxton
**Keywords**: robotics, Sunday Robotics, home robot, teleoperation, training data, glove-based collection, UMI, distributed workers, data-first approach

## Elevator pitch
Sunday Robotics is training home robots using $400 gloves worn by 500+ distributed operators rather than expensive robot hardware—eliminating three of four traditional data collection cost components by separating data collection from robot execution.

## Takeaways
- Sunday Robotics raised a $165M Series B to train robots using glove-based data collection instead of actual robots.
- The approach eliminates skilled operators, robot hardware, and teleoperation clones from the data collection stack—retaining only distributed human operators paid up to $60/hour.
- ~$400 gloves worn by operators, with identical tools mounted on "Memo" robot arm, create a direct correspondence between human and robot manipulation.
- Co-founder Cheng Chi developed the Universal Manipulation Interface (UMI), the underlying technology enabling this approach.
- 500+ distributed workers gather diverse, real-world training examples at scale.
- Data-first philosophy: significant engineering effort on gripper design and data collection before substantial model training.

## Synthesis
The core insight is separating data collection from robot deployment. Traditional robot training requires robots present during data collection—expensive machines operated by skilled technicians, creating bottlenecks on both hardware availability and operator expertise. Sunday's approach uses cheap glove hardware to capture the training signal (manipulation trajectories) while deferring the expensive hardware deployment to inference time.

The $400 glove vs. $50,000+ robot differential makes the economics transformative. If data quality transfers effectively from glove manipulation to robot execution, Sunday can scale data collection by deploying cheap hardware to distributed workers—paying $60/hour for valuable training trajectories—while keeping expensive robot hardware focused on what it's actually needed for (deployment).

The 500+ distributed worker model introduces quality control challenges that aren't present in traditional robotics data collection. When skilled technicians collect robot data in controlled environments, you can verify quality directly. When 500 distributed workers collect data in their homes with cheap gloves, data quality management requires different approaches—filtering, validation, weighting—to ensure training signal quality despite collection environment variability.

Chris Paxton's assessment flags the critical uncertainty: transfer dynamics between human tool manipulation and robot gripper execution aren't guaranteed to work well. If the glove-to-robot correspondence is imperfect, the training data may capture manipulation strategies that don't translate to the robot's physical constraints. The $165M bet is substantially on this transfer working—a fundamentally empirical question that the funding round implicitly answers partially (the data has been tested enough for investors to be convinced).
