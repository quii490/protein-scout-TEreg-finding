---
type: protein-evaluation
gene: "ANKRD23"
date: 2026-06-03
tags: [protein-scout, nucleoplasm, evaluation, full-reevaluate]
status: scored
---
## ANKRD23

Q86SG2 | Ankyrin repeat domain-containing protein 23 | 305aa | pLDDT 81.4 | PM=10 | norm=67.2/100

| 维度 | 得分 | 权重 | 加权 |
|---|---|---|---|---|
| 核定位特异性 | 7/10 | ×4 | 28 |
| 蛋白大小 | 4/10 | ×1 | 4 |
| 研究新颖性 | 10/10 | ×5 | 50 |
| 三维结构 | 6/10 | ×3 | 18 |
| 调控结构域 | 4/10 | ×2 | 8 |
| PPI 网络 | 5/10 | ×3 | 15 |
| **加权总分** | | | **123/180** |
| 互证加分 | | | +0.5 |
| **PubMed strict** | 10 | | |
| **归一化总分 (÷1.83)** | | | **67.2/100** |

**UniProt**: Q86SG2 — Nucleus (no evidence code). May be involved in energy metabolism; molecular link between myofibrillar stretch-induced signaling and muscle gene expression. GO-CC: actin cytoskeleton (IDA:HPA), cytosol (IDA:HPA), I band (IEA:Ensembl), intercalated disc (IEA:Ensembl), nucleoplasm (IDA:HPA), nucleus (IBA:GO_Central). Alias: DARP (Diabetes-Related Ankyrin Repeat Protein).

**HPA IF 状态**: HPA IF 原图未可靠获取（HPA 检索页无可用的 subcellular IF 原图）。核定位基于 HPA localization/reliability + UniProt + GO-CC。

### 核定位评定
HPA 主定位 Nucleoplasm 与 Cytosol 双定位 (Approved)，额外定位 Actin filaments。UniProt 注释为 Nucleus（无证据编码），GO-CC 丰富：nucleoplasm (IDA:HPA) + nucleus (IBA:GO_Central) + actin cytoskeleton + cytosol + I band + intercalated disc。核定位证据充分（HPA IF + GO-CC 实验证据），但 Cytosol 共主定位和肌节结构定位（I band、intercalated disc）显示该蛋白在骨骼肌/心肌中可能以细胞质-核双分布模式存在。评为 7/10。

### 蛋白大小
305 aa，34.3 kDa，小型蛋白。含 Ankyrin repeat (IPR002110/IPR036770/IPR050663)。Pfam: Ank (PF00023) + Ank_2 (PF12796)。小分子量便于重组表达纯化。评为 4/10。

### 研究新颖性
PubMed strict count = 10（≤20 档）。别名 DARP 反映其在糖代谢中的作用。关键文献：(1) PMID 28754631 (2017) — ANKRD23 负调控成肌细胞分化，是该蛋白最直接的功能研究；(2) PMID 26398569 (2015) — DARP/Ankrd23 通过调节骨骼肌 AMPK 活性修饰葡萄糖稳态；(3) PMID 39383190 (2024) — IL-11 治疗导致急性左心室功能障碍中涉及 ANKRD23。研究集中于肌肉能量代谢与分化，有一定功能数据但体量小。评为 10/10。

### PDB 结构
PAE 图像暂无数据（未生成本地图片或未可靠获取），结构判断基于 AlphaFold pLDDT 统计。
AlphaFold v6: mean_pLDDT = 81.4，pct_gt_90 = 60.0%，pct_70_90 = 13.8%，pct_lt_50 = 13.4%。置信度较好，60% 残基 pLDDT > 90。无实验 PDB 结构。AlphaFold 模型整体质量较高，可作为结构分析起点。评为 6/10。

### 调控结构域
InterPro: Ankyrin repeat (IPR002110/IPR036770/IPR050663)。Pfam: Ank (PF00023) + Ank_2 (PF12796)。纯 ANK 重复蛋白。功能指向肌细胞分化与代谢调控，ANK 重复可能作为信号转导支架。缺乏酶活性或核酸结合模块。评为 4/10。

### PPI 网络
STRING 请求失败（HTTP 502）。IntAct: NAP1L1 (Y2H)、FAM161B (Y2H array)、CTNNA3 (Y2H array)、CCDC6 (Y2H)、POLR3C (Y2H)、GRB2 (Y2H, SH3 信号适配器)、SMARCD1 (validated Y2H, SWI/SNF 染色质重塑)、KDM1A (Y2H, 组蛋白去甲基化酶) 等 15 条记录。UniProt curated: CCDC102B、CCDC57、CCDC6、CDCA7L、CLIC3、CTNNA3、GRB2、KDM1A、PIBF1、POLR3C、SMARCD1、SPRED1、TRIM41、YARS1 等 23 个伙伴。PPI 中含有 SMARCD1（染色质重塑）、KDM1A（组蛋白修饰）、POLR3C（RNA Pol III）等核蛋白，支持其核内功能。评为 5/10。

### 关键文献
- PMID 28754631: ANKRD23 negatively regulates myoblast differentiation (Gene, 2017)
- PMID 26398569: DARP/Ankrd23 modifies glucose homeostasis by modulating AMPK activity (PLoS One, 2015)
- PMID 39383190: IL-11 therapy causes acute left ventricular dysfunction (Cardiovasc Res, 2024)

### 人工复核建议
DARP 与糖尿病关联的研究背景使其在代谢-转录调控交叉领域具有独特价值。PPI 网络中 SMARCD1 和 KDM1A 均为染色质/表观遗传调控因子，暗示 ANKRD23 可能参与肌细胞中的染色质调控。建议进一步验证其核质穿梭机制及在肌肉基因表达调控中的具体角色。
