---
type: protein-evaluation
gene: "SLC67A1"
uniprot: "Q96BI1"
date: 2026-06-28
tags: [protein-scout, nucleus-cytoplasm, evaluation, rejected]
status: rejected
---

## SLC67A1 / Solute Carrier Family 67 Member A1 评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | SLC67A1 (别名: SLC22A18, BWR1A, IMPT1, ORCTL2, TSSC5) |
| 蛋白全称 | Solute carrier family 67 member A1 |
| UniProt ID | Q96BI1 (Swiss-Prot, reviewed) |
| 蛋白大小 | 424 aa |
| UniProt 证据等级 | 1: Evidence at protein level |
| 亚细胞定位 | **Apical cell membrane** (顶端细胞膜; 10次跨膜蛋白) |

### 2. 评分总览
| 维度 | 得分 | 权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 0/10 | x4 | 0.0 | 细胞膜多次跨膜转运蛋白 |
| 蛋白大小 | 5/10 | x1 | 5.0 | 424 aa |
| 新颖性 | 5/10 | x5 | 25.0 | PubMed=86 (实际为 SLC22A18); hotness=7 |
| 三维结构 | 2/10 | x3 | 6.0 | MFS fold; 10次跨膜螺旋 |
| 调控结构域 | 0/10 | x2 | 0.0 | MFS transporter domain; 无染色质/DNA结合域 |
| PPI | 3/10 | x3 | 9.0 | PPI degree=0 (BioGRID: 56) |
| **加权总分** | | | **45.0/180** | |
| **归一化总分** | | | **25.0/100** | |

### 3. 详细分析

**核定位: 完全不成立 (FAIL)**。SLC67A1 是一个**10 次跨膜的细胞膜转运蛋白**，定位在肾近曲小管的顶端膜表面 (apical membrane)。UniProt 标注 "Apical cell membrane; Multi-pass membrane protein"，10 个跨膜螺旋横跨整个膜。**该蛋白不可能存在于细胞核中**。HPA 的任何核定位标注为假阳性。

**功能**: 有机阳离子转运蛋白，可能基于质子外排反向转运机制运输有机阳离子。可能运输氯喹和奎尼丁类化合物。参与脂质代谢调控。属于 Major Facilitator Superfamily (MFS)。

**基因组位点特殊性**: SLC67A1 (原 SLC22A18) 位于 11p15.5 印记区域，与 Beckwith-Wiedemann 综合征相关。该位点的印记失调可能导致肿瘤发生。**这一印记特征可能误导筛选算法将其与染色质调控相关联**，但实际上该蛋白本身是膜转运蛋白，不参与染色质水平的调控。

**PubMed 数据说明**: esearch 中 PubMed 返回 86 篇文献，但查询被自动重映射至 "SLC22A18" (旧名称)。这些文献涉及印记基因、肿瘤发生和有机阳离子转运，无一涉及 TE 调控或染色质。

**PPI**: PPI degree=0 (筛选数据) 或 BioGRID 56 条连接。BioGRID 中的相互作用伙伴包括 PHLDA2、TSSC4、CDKN1C 等，均为同一位点 (11p15.5) 上的印记基因，反映的是基因组聚类而非功能互作。

**TE 调控潜力**: **零**。SLC67A1 是膜转运蛋白，其生物学功能为代谢物跨膜运输。虽然基因组位点 (11p15.5 印记区域) 具有表观遗传调控特征，但该蛋白本身不参与染色质修饰或转录调控。

### 4. 总体评价
**25.0/100** | **REJECTED**

**拒绝理由**: SLC67A1 是一个**细胞膜多次跨膜有机阳离子转运蛋白** (MFS 超家族)。其在筛选数据中获得 tier=2 和 hotness=7 可能来源于其基因组位点 (11p15.5 印记区域 Beckwith-Wiedemann syndrome locus) 的表观遗传特征被误判。该蛋白本身定位在细胞膜，不含任何 DNA 结合域或染色质调控结构域。Genecards 条目中存在 mouse symbol "Slc67a1" 混入的问题。
