---
type: protein-evaluation
gene: "MKLN1"
date: 2026-06-04
tags: [protein-scout, confirmed-rejected, critical-false-rejection-recheck]
status: confirmed-rejected
previous_status: rejected
previous_rejection_reason: nuclear_score ≤ 3
recheck_result: "CONFIRMED REJECTED — HPA=Plasma membrane+Cytosol(Approved); UniProt nucleoplasm仅ECO:0000250(by similarity); GO-CC nucleoplasm仅IEA(电子注释); CTLH E3 ligase降解HBP1 TF但自身不在核内; nuclear_score=2准确"
revised_nuclear_score: 2
---

## MKLN1 核蛋白评估报告 -- FALSE REJECTION RE-EVALUATION (确认拒绝)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | MKLN1 / Muskelin |
| 蛋白大小 | 735 aa / 84.8 kDa |
| UniProt ID | Q9UL63 |
| 蛋白全名 | Muskelin |
| HPA IF 主定位 | **Plasma membrane, Cytosol** |
| HPA IF 附加定位 | Vesicles |
| HPA Reliability | Approved |
| 原评估状态 | REJECTED (nuclear_score=2) |
| 重新评估日期 | 2026-06-04 |
| CONFIRMED REJECTED | **CONFIRMED REJECTED** — 非核蛋白 |

### 2. 评分总览（修订后，确认原评分）

| 维度 | 得分 | 权重 | 加权 | 摘要 |
|---|---|---|---|---|
| 核定位特异性 | **2/10** | ×4 | 8 | HPA=Plasma membrane+Cytosol(Approved); UniProt nucleoplasm仅ECO:0000250; GO-CC nucleoplasm仅IEA |
| 蛋白大小 | 4/10 | ×1 | 4 | 735aa/84.8kDa，中等偏大 |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=44 (41-60→6) |
| 三维结构 | 8/10 | ×3 | 24 | pLDDT=89.1; PDB 8TTQ (EM 3.27A, 全长二聚体) |
| 调控结构域 | 7/10 | ×2 | 14 | LisH+CTLH+Kelch×6; E3泛素连接酶底物识别模块 |
| PPI网络 | 6/10 | ×3 | 18 | STRING: RANBP9(0.998), GID8(0.995), RMND5A(0.990); CTLH/GID复合物全实验验证 |
| **加权总分** | | | **98/180** | |
| **归一化总分 (÷1.8)** | | | **54.4/100** | |

### 3. False rejection recheck -- CRITICAL

**为何被列为CRITICAL进行重新评估:**

MKLN1又名Muskelin，是CTLH/GID E3泛素连接酶复合物的核心支架亚基，该复合物直接靶向转录因子HBP1进行泛素化降解。这种"E3连接酶在胞质中降解核转录因子"的功能模式引发了合理的疑问: MKLN1是否也在核内执行部分功能? 本研究池中已有多个E3连接酶亚基(如ANAPC13)被列为候选，因此MKLN1值得仔细审查。

此外，MKLN1拥有所有10个CRITICAL基因中最好的结构数据组合(AlphaFold pLDDT 89.1 + 全长PDB 8TTQ + LisH/CTLH/Kelch多重结构域)和最丰富的结构域架构(9个InterPro条目)。

**逐一数据库审查:**

1. **UniProt Subcellular Location (harvest packet)**:
   - Cytoplasm: ECO:0000269 (IDA, 实验验证) -- 高证据
   - Cytoplasm, cytosol: ECO:0000250 (by similarity) -- 推断
   - **Nucleus, nucleoplasm: ECO:0000250 (by similarity) -- 仅为序列相似性推断，非人源实验证据**
   - Cell projection, ruffle: ECO:0000250
   - Cytoplasm, cell cortex: ECO:0000250
   - Synapse: ECO:0000250
   - Postsynapse: ECO:0000250
   - **7个亚细胞定位中，仅1个是实验验证(IDA)，其余6个均为by similarity(ECO:0000250)。核定位恰为by similarity**

2. **GO-CC (harvest packet) -- 核定位仅为电子注释**:
   - GO:0005737 cytoplasm: IDA:UniProtKB (实验验证)
   - GO:0000151 ubiquitin ligase complex: IDA:UniProtKB (实验验证)
   - GO:0005654 nucleoplasm: **IEA:UniProtKB-SubCell (电子自动注释!!)**
   - 其他6个GO-CC术语(细胞皮层、突触、GABA-ergic synapse等)均为ISS/IEA
   - **nucleoplasm的GO-CC证据是IEA(最低等级)，无任何人工审核或实验验证**

3. **HPA Subcellular (harvest packet) -- 决定性**:
   - Main location: **Plasma membrane**, **Cytosol**
   - Additional: Vesicles
   - Reliability: **Approved (最高可信度!!)**
   - IF display images: 6张在线可用
   - **零核信号!! 完全没有nucleoplasm/nucleus/nuclear membrane**

4. **功能证据 -- 胞质E3连接酶靶向核内转录因子**:
   - CTLH/GID E3连接酶复合物介导HBP1转录因子的泛素化降解
   - HBP1在核内调控基因表达，但其降解发生在胞质(蛋白酶体)
   - Muskelin作为支架亚基在胞质中组装CTLH/GID复合物
   - 功能还包括GABA受体(GABRA1)从细胞膜的内吞
   - 介导细胞铺展和细胞骨架对THBS1的响应
   - **靶向转录因子进行降解 =/= 自身定位于核内**

**为何这不是假阴性:**

MKLN1的三个核定位数据点均来自低证据等级的推断:
- UniProt nucleoplasm: ECO:0000250 (by similarity — 基于其他物种或相似蛋白的推断，可能是小鼠Muskelin有核定位)
- GO-CC nucleoplasm: IEA (电子自动注释 — 由pipeline自动从UniProt序列推断)
- GO-CC没有其他核术语

而HPA Approved的实验数据明确否定核定位: Plasma membrane + Cytosol + Vesicles，零核信号。

MKLN1的案例说明了一个重要原则: E3泛素连接酶虽然靶向核转录因子(HBP1)进行降解，但其泛素化反应通常发生在胞质——E3连接酶识别从核中输出的底物、催化泛素链组装、最终将底物递送至26S蛋白酶体。而蛋白酶体本身可以定位于胞质和核。

**修订后核定位评分: 2/10 (确认)**。

### 4. 详细分析

#### 4.1 核定位证据

| 来源 | 定位 | 可信度 | 证据代码 |
|------|------|--------|----------|
| HPA (IF) | Plasma membrane, Cytosol | **Approved** (最高) | IF实验，6张display images |
| HPA (IF) | Vesicles (additional) | Approved | IF实验 |
| UniProt | Cytoplasm | IDA | ECO:0000269 (实验) |
| UniProt | Nucleoplasm | ECO:0000250 | **by similarity (推断)** |
| GO-CC | cytoplasm | IDA:UniProtKB | 实验 |
| GO-CC | nucleoplasm | IEA:UniProtKB-SubCell | **电子注释** |
| GO-CC | ubiquitin ligase complex | IDA:UniProtKB | 实验 |

Muskelin的"核定位"证据完全来自两个低层级推断(UniProt by similarity + GO IEA)，而HPA Approved实验数据明确将其定位于Plasma membrane+Cytosol。**核定位评分: 2/10 (确认)**。

#### 4.2 蛋白大小评估

735 aa / 84.8 kDa。中等偏大的多结构域蛋白，包含LisH(二聚化)+CTLH(复合物组装)+Kelch×6(beta-propeller底物识别)。实验操作可能有一定难度(大蛋白表达+纯化)。**评分: 4/10**。

#### 4.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict_count | 44 |
| PubMed symbol_only | 77 |
| 主要方向 | CTLH/GID复合物、结直肠癌易感、肝癌lncRNA |

中等新颖度(44篇)。研究集中在CTLH/GID E3连接酶复合物的生化特性和癌症关联。**评分: 6/10**。

**关键文献**:
1. Yun D et al. (2025). "MMP14 and MKLN1 as colorectal cancer susceptibility genes." *J Transl Med*. PMID: 40369569
2. Guo C et al. (2022). "SOX9/MKLN1-AS Axis Induces Hepatocellular Carcinoma." *Biochem Genet*. PMID: 35138470
3. Barbulescu P et al. (2024). "FAM72A degrades UNG2 through the GID/CTLH complex." *Nat Commun*. PMID: 39215025
4. Liu H et al. (2020). "The GID ubiquitin ligase complex regulates AMPK activity and lifespan." *Autophagy*. PMID: 31795790
5. Lampert F et al. (2018). "The multi-subunit GID/CTLH E3 ubiquitin ligase targets Hbp1 for degradation." *eLife*. PMID: 29911972

#### 4.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 平均 pLDDT | 89.1 |
| pLDDT > 90 (Very High) | 71.3% |
| pLDDT < 50 (Low) | 4.4% |
| 实验结构 (PDB) | 8TTQ (EM, 3.27A, chains A/B=2-735, 全长二聚体) |

PDB 8TTQ是CTLH/GID E3连接酶复合物的冷冻电镜全结构，覆盖Muskelin全长并展示其二聚化模式。N端LisH-CTLH介导与GID8/RANBP9的互作; C端6个Kelch重复形成beta-propeller负责底物识别。结构质量优秀。**评分: 8/10**。

#### 4.5 结构域分析

9个InterPro条目，3个Pfam条目。LisH domain (IPR006594, dimerization) + CTLH domain (IPR010565, complex assembly) + Kelch repeats ×6 (IPR006652, IPR015915, beta-propeller)。结构域在E3泛素连接酶底物识别中的角色清晰。

**与TE调控的潜在关联**: CTLH/GID复合物通过降解HBP1(TE-associated transcription factor?)间接影响转录。但Muskelin本身作为胞质支架，不直接接触染色质。Kelch beta-propeller的底物识别功能可能靶向TE来源的蛋白底物，但这属于推测。**评分: 7/10**。

#### 4.6 PPI 网络

| Partner | Combined Score | Experimental | 功能 |
|---------|---------------|--------------|------|
| RANBP9 | 0.998 | 0.837 | CTLH复合物亚基 |
| GID8 | 0.995 | 0.701 | CTLH复合物亚基 |
| RMND5A | 0.990 | 0.835 | CTLH复合物亚基 |
| WDR26 | 0.961 | 0.671 | CTLH复合物亚基 |

PPI网络全部集中于CTLH/GID复合物(STRING/IntAct高度一致)，IntAct确认RMND5A、GID4、MAEA、TLE4、SLX4等co-IP。实验证据扎实但反映胞质E3连接酶功能。**评分: 6/10**。

### 5. 最终决定

**CONFIRMED REJECTED — 非核蛋白，nuclear_score=2准确**

Muskelin是一个高度有序的胞质E3连接酶支架蛋白，其结构数据(AlphaFold+PDB)和PPI网络(CTLH/GID)在10个CRITICAL基因中属于最优。但由于HPA Approved明确显示Plasma membrane+Cytosol(零核信号)，且UniProt/GO-CC的核定位均为低层级推断，nuclear_score=2是正确的。

**与其他E3连接酶基因的比较**: ANAPC13(APC/C复合物亚基)也在此批次中被拒绝——两者均为E3泛素连接酶复合物亚基但在执行功能时不在核内。而AKIRIN1(Akirin-1)虽与蛋白酶体/PPI相关但明确在核内(HPA Approved Nucleoplasm)。每个E3连接酶亚基的亚细胞定位需要根据实验证据单独判断，不能一概而论。

**不建议重新评估**。除非有新的实验数据显示Muskelin在特定条件下(如细胞应激、分化)发生核转位。

### 6. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9UL63
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9UL63
- PDB: https://www.rcsb.org/structure/8TTQ
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=MKLN1%5BTitle/Abstract%5D
- HPA: https://www.proteinatlas.org/ENSG00000128585-MKLN1
- STRING: https://string-db.org/network/9606.ENSP00000323527
- IntAct: https://www.ebi.ac.uk/intact/interactors/id:Q9UL63
- Harvest packet: /Users/quii/Desktop/projects/TE-regulated proteins finding/protein_data/harvest_packets/MKLN1.json (2026-06-03)

HPA IF图像在线可用(6张blue_red_green, Plasma membrane+Cytosol信号)，未下载本地。PAE未生成本地。
