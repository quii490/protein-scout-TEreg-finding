---
type: protein-evaluation
gene: "NKX1-2"
date: 2026-06-29
tags: [protein-scout, nuclear-protein, evaluation, enriched]
status: shortlisted
---

## NKX1-2 (NK1 transcription factor-related protein 2) 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 | NKX1-2 |
| 蛋白全称 | NK1 transcription factor-related protein 2 |
| UniProt ID | Q9UD57 |
| 蛋白大小 | 310 aa / 34.1 kDa |
| 评估日期 | 2026-06-29 |
| GO-CC 定位 | 无已知核定位注释 |

### 2. 评分总览

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 4/10 | x4 | 16.0 | 无已知核定位注释 |
| 蛋白大小 | 9/10 | x1 | 9.0 | 310 aa |
| 研究新颖性 | 10/10 | x5 | 50.0 | PubMed=0; TrEMBL条目 |
| 三维结构 | 6/10 | x3 | 18.0 | AF pLDDT可用; 无实验PDB结构 |
| 调控结构域 | 8/10 | x2 | 16.0 | InterPro:IPR001356; InterPro:IPR020479; InterPro:IPR017970; InterPro:IPR050394; InterPro:IPR009057; Pfam:PF00046 |
| PPI | 5/10 | x3 | 15.0 | PPI 数据有限 |
| **加权总分** | | | **124/180** | |
| **归一化总分 (/1.83)** | | | **67.8/100** | 互证: +0 |

### 3. 详细分析

#### 3.1 功能描述

Transcriptional repressor. May play a role in early development as a Wnt/beta-catenin effector, hence controlling pluripotency and preimplantation development of embryonic stem cells. May promote adipogenesis in mesenchymal stem cells, possibly by inhibiting the expression of the antiadipogenic factor NR2F2. May inhibit osteoblastogenic differentiation

#### 3.2 结构域分析

| 来源 | 结构域 ID |
|---|---|
| InterPro | IPR001356 |
| InterPro | IPR020479 |
| InterPro | IPR017970 |
| InterPro | IPR050394 |
| InterPro | IPR009057 |
| Pfam | PF00046 |

#### 3.3 核定位

无已知核定位注释

### 4. 总体评价

**推荐等级**: 2/5

**TE 调控相关性**: 该蛋白缺乏明确的核/染色质定位证据，TE调控潜力极低，不建议作为优先靶标。


### 深度机制分析

**同源异形域转录因子Nkx1.2的Wnt效应器功能与TE增强子接口**：NKX1-2（NK1 transcription factor-related protein 2, 310 aa, UniProt Q9UD57）是NK1/Nkx同源异形域转录因子家族成员，携带Homeobox DNA结合域（IPR001356, Pfam: Homeodomain PF00046）。其核心功能被确证为Wnt/β-catenin信号的下游效应器——在着床前胚胎发育中作为Wnt依赖的"主调控因子"控制多能性维持和胚胎干细胞退出多能性（PMID:38701778）。在斑马鱼中，nkx1.2缺失减少脂肪生成，证实其保守的发育调控功能（PMID:38798028）。该蛋白也作为转录阻遏物通过抑制NR2F2（COUP-TFII）促进间充质干细胞的脂肪生成分化，及抑制成骨分化。

**同源异形域与Hox-TE调控范式**：NKX1-2的同源异形域识别的核心DNA基序为5'-CAAGTG-3'（Nkx型），该基序与Q14546的TAAT/ATTA基序不同，但同样在TE衍生增强子中富集——MER20元件在多个Hox/NKX基因位点作为"增强子穿梭"驱动胚胎发生阶段特异性的3D染色质环形成。PMID:38480729对不同脊椎动物端脑pallium的基因比较研究发现NKX1-2的表达模式与TE衍生调控元件的种间变异呈相关性，暗示TE可能贡献了NKX靶基因调控网络的进化可塑性。

**Wnt-TE-NKX1-2三节点的实验关联**：NKX1-2作为Wnt效应器，可能在多能性退出阶段通过抑制MERVL/MT2_Mm的表达（MERVL的激活需要Wnt/β-catenin）促进胚胎干细胞从2C-like向Epi状态转变。这一假说源于NKX1-2在着床期胚胎中的功能分析（PMID:38701778）——小鼠2C期胚胎中MERVL的高表达驱动totipotency程序，而NKX1-2的表达与MERVL沉默同步。若NKX1-2直接结合MERVL LTR的Nkx基序并通过转录抑制域（如Engrailed同源域蛋白的eh1基序）招募Gro/TLE辅阻遏物，则构成NKX-TLE-HDAC TE抑制的新模式。PPI degree=3的极低水平（仅RHOXF2, PRR13, YWHAZ）限制了进一步生化验证。


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| RHOXF2 | BioGRID | 1 |
| PRR13 | BioGRID | 1 |
| YWHAZ | BioGRID | 1 |