---
id: usability
title: Usability
aliases: [usability (ISO 9241-11)]
page_type: construct
template_version: "0.1"
fields: [hci]

broader: [task-characteristics]

status: ai-draft
last_reviewed: null
reviewers: []

sources: [iso9241-11, hornbaek2007]
---

# Usability

> How well specified users can reach specified goals with a system: effectively, efficiently, and with satisfaction, in a specified context.

## 1. Definition
ISO 9241-11 defines usability as the extent to which specified users can use a system to achieve specified goals with effectiveness, efficiency, and satisfaction in a specified context of use [iso9241-11]. A system has more usability when its users reach their goals more completely, with fewer resources, and with a better experience.

## 2. Boundaries
Usability is a property of the system *for given users, goals, and context*, not of the system alone. It is broader than ease of learning or look and feel. It overlaps with, but is not the same as, usefulness (whether the system's functions serve the goal at all). It sits under [task characteristics](task-characteristics.md) for that reason.

## 3. Narrower constructs
The ISO definition splits usability into effectiveness, efficiency, and satisfaction. Here the first two are [task effectiveness](task-effectiveness.md) and [task efficiency](task-efficiency.md), which also sit under [task performance](task-performance.md); satisfaction appears as [perceived usability](perceived-usability.md), and [interaction friction](interaction-friction.md) is added for the extra work a system imposes. The parts correlate only modestly, so improving one does not guarantee the others [hornbaek2007].
<!-- generated:narrower:start -->
- [Interaction friction](interaction-friction.md)
- [Task effectiveness](task-effectiveness.md)
- [Task efficiency](task-efficiency.md)
- [Usability: perceived usability](perceived-usability.md)
<!-- generated:narrower:end -->

## 4. Metrics
No single metric covers usability. Pick at least one metric per narrower construct.
<!-- generated:metrics:start -->
_No metric page yet._
<!-- generated:metrics:end -->

## 5. Links to business objectives
This construct is business objective 2, [Improved Usability](../objectives/improved-usability.md). Its link to [Sustained Use](../objectives/sustained-use.md) is theoretical (via perceived ease of use and satisfaction).

## 6. How it is identified
Standard definition [iso9241-11].

## 7. Sources
- [iso9241-11]
- [hornbaek2007]

## Open questions and review notes
- Should usefulness be a sibling construct under a root such as "value to the user"?
