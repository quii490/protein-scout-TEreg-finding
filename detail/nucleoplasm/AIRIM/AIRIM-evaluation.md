---
type: protein-evaluation
gene: "AIRIM"
date: 2026-06-04
tags: [protein-scout, rescored, rescued-to-scored, critical-false-rejection]
status: rescored-to-scored
previous_status: scored
previous_rejection_reason: nuclear_score ≤ 3
rescue_reason: "GO-CC nucleolus/nucleoplasm(IDA:HPA)+UniProt Nucleus(IDA); function=chromatin-associated; PDB 8RHN全长; Extremely novel(2 papers); nuclear_score=3 was an error"
revised_nuclear_score: 6
---

## AIRIM 核蛋白评估报告 -- CRITICAL FALSE REJECTION RE-EVALUATION

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | AIRIM / C1orf109 |
| 蛋白大小 | 203 aa / 23.4 kDa |
| UniProt ID | Q9NX04 |
| 蛋白全名 | AFG2-interacting ribosome maturation factor |
| HPA IF 主定位 | (无IF数据) |
| HPA Reliability | (无) |
| 原评估状态 | REJECTED (nuclear_score=3) |
| 重新评估日期 | 2026-06-04 |
| 重新评估结果 | **RESCUED TO SCORED** |

### 2. 评分总览（修订后）

| 维度 | 得分 | 权重 | 加权 | 摘要 |
|---|---|---|---|---|
| 核定位特异性 | **6/10** | ×4 | 24 | HPA无IF; GO-CC nucleolus+nucleoplasm(IDA:HPA); UniProt Nucleus(IDA); Function=chromatin-associated 55LCC |
| 蛋白大小 | 5/10 | ×1 | 5 | 203aa/23.4kDa，极小蛋白 |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=2 (≤20→10) |
| 三维结构 | 9/10 | ×3 | 27 | pLDDT=94.2; PDB 8RHN (EM 4.50A, 全长) |
| 调控结构域 | 5/10 | ×2 | 10 | IPR029159; chromatin-associated 55LCC ATPase复合体组分 |
| PPI网络 | 3/10 | ×3 | 9 | STRING 404; IntAct: 大量Y2H+少数co-IP(CINP, TADA2A) |
| **加权总分** | | | **125/180** | |
| **归一化总分 (÷1.8)** | | | **69.4/100** | |

### 3. False rejection recheck -- CRITICAL

**为何本次重新评估被列为CRITICAL:**

AIRIM在极度新颖(仅2篇PubMed, 其中一篇为Nature Cell Biology)且结构优质(pLDDT 94.2 + 全长PDB 8RHN)的情况下因nuclear_score=3被错误拒绝。核心争议点在于HPA没有可用的IF图像，但GO-CC的nucleolus(IDA:HPA)和nucleoplasm(IDA:HPA)注释来自HPA本身——这说明HPA实际上有实验数据，只是IF原图在API检索时未成功获取。此外，AIRIM的UniProt功能描述明确写有"chromatin-associated"，这对核蛋白评估具有决定性意义。

**逐一数据库审查:**

1. **UniProt Subcellular Location (harvest packet)**:
   - Nucleus: ECO:0000269 (IDA, 实验验证)
   - Cytoplasm: ECO:0000269 (IDA, 实验验证)
   - 双定位，但均为实验验证

2. **GO-CC (harvest packet) -- 关键的核定位数据来源于HPA**:
   - GO:0005730 nucleolus: IDA:HPA
   - GO:0005654 nucleoplasm: IDA:HPA
   - GO:0005634 nucleus: IDA:UniProtKB
   - GO:0005737 cytoplasm: IDA:UniProtKB
   - GO:0005829 cytosol: IDA:HPA
   - **nucleolus和nucleoplasm的注释来自IDA:HPA，这意味着HPA实际有定位数据，并非真正的"无数据"**

3. **HPA Subcellular (harvest packet)**:
   - status: "page_found_no_if_image_detected"
   - subcellular_location: [] (空)
   - **但GO-CC的IDA:HPA注释证明HPA有实验数据，只是IF原图未被harvest script下载**

4. **功能证据 -- CHROMATIN-ASSOCIATED**:
   - UniProt function: "Part of the 55LCC heterohexameric ATPase complex which is **chromatin-associated** and promotes replisome proteostasis to maintain replication fork progression and genome stability"
   - **"chromatin-associated"是直接来自UniProt的描述，这应该大幅提升核定位评分**

5. **PDB证据**:
   - 8RHN: EM 4.50A, 全长(1-203), 55LCC复合物结构
   - 提供了AIRIM在大型蛋白复合物中的结构背景

**为何原核定位评分=3是错误的:**

原评估认为"HPA 无可用的 IF 图像数据"就降低了核定位评分，但忽略了:
- GO-CC nucleolus和nucleoplasm的注释正是来自HPA (IDA:HPA)
- UniProt明确标注"chromatin-associated"
- UniProt Nucleus为IDA实验证据
- 虽然也定位于Cytoplasm(参与核糖体60S成熟)，但chromatin-associated的功能定义使其核蛋白身份不容置疑

**修订后核定位评分: 6/10**
- GO-CC nucleolus/nucleoplasm (IDA:HPA): HPA来源的实验证据(尽管IF图未下载)
- UniProt Nucleus (ECO:0000269 IDA): 独立实验验证
- Function "chromatin-associated": 功能核定位的最强证据
- 扣分项: 同时定位于Cytoplasm(IDA); HPA IF原图未成功下载; 核定位特异性非100%
- 因nucleolus+nucleoplasm双核亚区室+chromatin-associated功能，核定位评分不得低于5/10

### 4. 详细分析

#### 4.1 核定位证据

| 来源 | 定位 | 可信度 | 证据代码 |
|------|------|--------|----------|
| HPA (IF) | 无IF下载 | N/A | API检索未获取到IF原图 |
| UniProt | Nucleus | IDA | ECO:0000269 |
| UniProt | Cytoplasm | IDA | ECO:0000269 |
| GO-CC | nucleolus | IDA:HPA | HPA实验来源 |
| GO-CC | nucleoplasm | IDA:HPA | HPA实验来源 |
| GO-CC | nucleus | IDA:UniProtKB | 实验验证 |
| GO-CC | cytoplasm | IDA:UniProtKB | 实验验证 |
| GO-CC | cytosol | IDA:HPA | HPA实验来源 |
| UniProt Function | **chromatin-associated** (55LCC complex) | PMID:38554706 | Nature 2024 |

AIRIM的核定位证据基于三线汇合: (1) UniProt Nucleus IDA; (2) GO-CC nucleolus/nucleoplasm IDA:HPA (HPA本身有实验支持); (3) Function "chromatin-associated" (55LCC复合体直接与染色质结合)。染色质关联性是10个CRITICAL基因中除AKIRIN1 (GO-CC chromatin)外最强的核功能证据。55LCC复合体在S期被复制叉DNA激活，在染色质上切割replisome底物——这要求AIRIM(作为复合体组分)定位于染色质/核。**修订评分: 6/10**。

#### 4.2 蛋白大小评估

203 aa / 23.4 kDa。极小蛋白，仅含单一AIRIM家族结构域(PF15011, DUF4520)。作为55LCC异六聚体ATPase复合体的一个亚基，其小尺寸可能反映特定支架功能。实验操作(表达/纯化/标签)便利。**评分: 5/10**。

#### 4.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict_count | 2 |
| PubMed symbol_only | 2 |
| 别名 | C1orf109 |
| 主要方向 | 核糖体成熟、神经发育、复制叉稳定性 |

PubMed仅2篇(strict)，是所有基因中最少的(与少数其他基因并列)。2024-2025年的两篇论文(一篇Nature Cell Biology, 一篇bioRxiv)由同一课题组发表，揭示了AIRIM在核糖体成熟和复制叉稳定性中的全新功能。基因原名C1orf109(2024年前)，2024年才被正式命名为AIRIM。**评分: 10/10** (≤20篇，极端新颖)。

**关键文献**:
1. Ni C et al. (2025). "A programmed decline in ribosome levels governs human early neurodevelopment." *Nat Cell Biol*. PMID: 40760247 -- 核心CNS文献，揭示ribosome水平与神经发育
2. Ni C et al. (2024). "An inappropriate decline in ribosome levels drives a diverse set of neurodevelopmental disorders." *bioRxiv*. PMID: 38260472 -- 预印本，扩展到神经发育疾病

#### 4.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 平均 pLDDT | 94.2 |
| pLDDT > 90 (Very High) | 87.7% |
| pLDDT 70-90 (High) | 10.8% |
| pLDDT 50-70 (Medium) | 1.0% |
| pLDDT < 50 (Low) | 0.5% |
| 有序区域 (pLDDT>70) | 98.5% |
| 实验结构 (PDB) | 8RHN (EM, 4.50A, chains A/B=1-203, 全长) |

仅0.5%残基pLDDT<50，98.5%高度有序。AlphaFold 94.2的平均pLDDT在10个CRITICAL基因中最高(与AFMID的94.0并列)。8RHN为低温电镜结构(4.50A)，虽然分辨率中等但覆盖全长1-203。**评分: 9/10**。

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

#### 4.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro | IPR029159 (AIRIM/C1orf109 family) |
| Pfam | PF15011 (DUF4520, C1orf109 family) |

AIRIM为单结构域蛋白，属于55LCC异六聚体ATPase复合体的组成部分。功能为"chromatin-associated"的复制体蛋白酶稳态维持因子，促进replisome底物的蛋白水解从染色质上清除以确保DNA复制和mitotic fidelity。

**与TE调控的潜在关联**: (1) 55LCC复合体在染色质上的复制叉处发挥功能——转座子(TE)在复制过程中的不适当活性可导致基因组不稳定性，55LCC通过处理replisome底物可能间接影响TE区域的复制保真度; (2) 核糖体成熟功能与翻译调控相关，翻译水平的TE调控是新兴领域; (3) 55LCC ATPase活性被复制叉DNA特异性增强，这提示AIRIM可能感知特定DNA结构(如TE形成的非B型DNA)。**评分: 5/10** (从4调至5，因chromatin-associated功能)。

#### 4.6 PPI 网络

STRING返回404错误(无网络数据)。UniProt记录的大量互作(>100个伙伴)几乎全为Y2H高通量筛选(experiments=3-6)，仅少数基因(CINP experiments=15, TADA2A experiments=6)有更多实验证据。IntAct确认的主要互作包括:
- CINP: co-IP (PMID:28514442) -- CDK2-interacting protein, 复制叉保护
- TADA2A: Y2H array (PMID:32296183) -- 转录adaptor, SAGA复合物亚基
- ZBED1: Y2H array -- 锌指BED-type, DNA结合/转座酶起源
- IKZF3: Y2H array -- 转录因子, 淋巴细胞发育
- IHO1: Y2H array -- 减数分裂DNA双链断裂起始因子

TADA2A(SAGA组蛋白乙酰转移酶复合物亚基)和ZBED1(转座酶起源的DNA结合蛋白)的互作具有调控意义。**评分: 3/10**。

### 5. Rescue Decision

**决策: RESCUED TO SCORED**

**核定位评分修正**: 从3/10 → 6/10。修正依据:
1. GO-CC nucleolus + nucleoplasm 均来自IDA:HPA (HPA有实验数据，非真正"无数据")
2. UniProt Function明确描述"chromatin-associated" (55LCC complex)
3. UniProt Nucleus (ECO:0000269 IDA)
4. PDB 8RHN展示全长蛋白的chromatin-associated功能状态

**修正后加权总分**: 125/180 (69.4/100)。

**尽管结构域组成简单且为小蛋白，AIRIM应进入scored蛋白列表。其"chromatin-associated"功能属性 + Nature Cell Biology级别的文献 + 极端新颖(2篇) + 高质量PDB结构使其成为探索染色质复制叉区域TE调控的有趣候选。特别是55LCC复合体在S期被复制叉DNA激活这一特性，可能与TE的细胞周期依赖性表达调控有关。**

### 6. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9NX04
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9NX04
- PDB: https://www.rcsb.org/structure/8RHN
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=AIRIM%5BTitle/Abstract%5D
- HPA: https://www.proteinatlas.org/search/AIRIM
- Harvest packet: /Users/quii/Desktop/projects/TE-regulated proteins finding/protein_data/harvest_packets/AIRIM.json (2026-06-03)

HPA IF原图未下载。GO-CC IDA:HPA注释来自HPA实验。PAE未生成本地。

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9NX04-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9NX04 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR029159; |
| Pfam | PF15011; |

### humanPPI / HPA Interaction
Source: 未找到 HPA interaction 页面

未从 HPA Interaction 页面解析到互作伙伴；需人工复核或使用其他 humanPPI 来源。
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
