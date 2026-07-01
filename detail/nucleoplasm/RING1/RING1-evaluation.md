---
type: protein-evaluation
gene: "RING1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## RING1 — REJECTED (研究热度过高 (PubMed strict=213，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | RING1 / RING1A, RNF1 |
| 蛋白名称 | E3 ubiquitin-protein ligase RING1 |
| 蛋白大小 | 406 aa / 42.4 kDa |
| UniProt ID | Q06587 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Cytosol; UniProt: Nucleus; Nucleus speckle |
| 蛋白大小 | 10/10 | ×1 | 10 | 406 aa / 42.4 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=213 篇 (>100→REJECTED) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=70.0; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR032443, IPR043540, IPR001841, IPR013083, IPR017 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 0.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **82.5/180** | |
| **归一化总分** | | | **45.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Cytosol | Approved |
| UniProt | Nucleus; Nucleus speckle | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytosol (GO:0005829)
- nuclear speck (GO:0016607)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- PcG protein complex (GO:0031519)
- PRC1 complex (GO:0035102)
- sex chromatin (GO:0001739)
- ubiquitin ligase complex (GO:0000151)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 213 |
| PubMed broad count | 339 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: RING1A, RNF1 |

**关键文献**:
1. Targeting UBE2T Potentiates Gemcitabine Efficacy in Pancreatic Cancer by Regulating Pyrimidine Metabolism and Replication Stress.. *Gastroenterology*. PMID: 36842710
2. RING1 missense variants reveal sensitivity of DNA damage repair to H2A monoubiquitination dosage during neurogenesis.. *Nature communications*. PMID: 39256363
3. Evolving Role of RING1 and YY1 Binding Protein in the Regulation of Germ-Cell-Specific Transcription.. *Genes*. PMID: 31752312
4. Perception of viral infections and initiation of antiviral defence in rice.. *Nature*. PMID: 40074903
5. Extensive folding variability between homologous chromosomes in mammalian cells.. *Molecular systems biology*. PMID: 40329044

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 70.0 |
| 高置信度残基 (pLDDT>90) 占比 | 25.6% |
| 置信残基 (pLDDT 70-90) 占比 | 30.8% |
| 中等置信 (pLDDT 50-70) 占比 | 11.1% |
| 低置信 (pLDDT<50) 占比 | 32.5% |
| 有序区域 (pLDDT>70) 占比 | 56.4% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=70.0，有序区 56.4%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR032443, IPR043540, IPR001841, IPR013083, IPR017907; Pfam: PF16207, PF13923 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| YAF2 | 0.999 | 0.873 | — |
| BMI1 | 0.999 | 0.960 | — |
| PCGF6 | 0.999 | 0.899 | — |
| PCGF3 | 0.999 | 0.820 | — |
| CBX4 | 0.999 | 0.886 | — |
| PHC1 | 0.999 | 0.822 | — |
| CBX8 | 0.999 | 0.901 | — |
| RNF2 | 0.999 | 0.880 | — |
| PCGF2 | 0.999 | 0.935 | — |
| RYBP | 0.999 | 0.940 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| — | — | — |

**PPI 互证分析**:
- 仅STRING预测
- STRING partners: 15，IntAct interactions: 0
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 0 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=70.0 + PDB: 无 | pLDDT=70.0, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus; Nucleus speckle / Nucleoplasm; 额外: Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. RING1 — E3 ubiquitin-protein ligase RING1，研究基础较多，新颖性有限。
2. 蛋白大小406 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 213 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 213 > 100，研究热度过高，不符合novelty筛选标准。**

### 深度机制分析

RING1/RING1A/RNF1（E3 ubiquitin-protein ligase RING1, 406 aa, 42.4 kDa, UniProt Q06587）是多梳抑制复合体1（PRC1）的核心催化亚基，其域架构由N端RING型锌指结构域（aa47-96, SMART:SM00184, Pfam:PF13923, InterPro:IPR001841）和C端RAWUL域（RING1 and WDR77-associated ubiquitin-like, Pfam:PF16207, IPR032443）组成，属于RING型E3连接酶超家族（IPR043540, IPR013083, IPR017907）。RING域通过Cys3HisCys4（C3HC4）锌配位模式（cross-brace结构——第一个和第三个Zn2+配位对与第二个和第四个交替排列）形成刚性平台，用于同时结合E2泛素偶联酶（如UBE2D/UBCH5A或UBE2E）和底物识别模块。AlphaFold v6 pLDDT=70.0（高置信25.6%, 有序区仅56.4%，低置信32.5%）表明RING1整体折叠为部分无序——在PRC1复合体内，RING1必须与BMI1/PCGF蛋白形成异源二聚体才能正确折叠并激活E3活性（这是经典的RING-RING二聚催化机制）。PDB无完整RING1结构（PDB=0），但RING1-BMI1异源二聚体的相关结构（如PDB 2CKL和4R8P）已充分验证此机制。HPA确认Nucleoplasm定位（Approved），GO-CC额外注释PcG protein complex（GO:0031519）、PRC1 complex（GO:0035102）、sex chromatin（GO:0001739）和ubiquitin ligase complex（GO:0000151）。

PPI互作网络完美映射了PRC1复合体的分层组装逻辑：(1) PCGF亚基（BMI1/PCGF4: combined score=0.999, 实验=0.960; PCGF2/MEL18: 0.999, 实验=0.935; PCGF3: 0.999, 实验=0.820; PCGF6/MBLR: 0.999, 实验=0.899）——RING1的异源二聚化伙伴，每个PCGF定义一种PRC1亚型（canonical vs variant PRC1）；(2) CBX/Chromobox亚基（CBX4/PC2: 0.999, 实验=0.886; CBX8/PC3: 0.999, 实验=0.901）——H3K27me3阅读器，通过chromodomain识别多梳标记并介导染色质结合；(3) PHC/多同源蛋白亚基（PHC1: 0.999, 实验=0.822）——通过SAM域聚合形成多梳小体(Polycomb bodies)的超分子组装；(4) RYBP/YAF2（RYBP: 0.999, 实验=0.940; YAF2: 0.999, 实验=0.873）——RYBP/YAF2与CBX在PRC1中是相互排斥的结合伙伴，定义非典型（variant）PRC1与典型（canonical）PRC1。RNF2/RING1B（0.999, 实验=0.880）是RING1的旁系同源物——两者在PRC1中可能替换或协同。

深度机制：RING1作为PRC1的催化核心执行H2AK119单泛素化（H2AK119ub1）——这是多梳基因沉默的基石标记。具体路径：PRC2首先沉积H3K27me3→CBX chromodomain识别H3K27me3→PRC1被招募至染色质→RING1-BMI1二聚体以E2~Ub硫酯作为泛素供体→RING1的RING域将泛素转移至核小体组蛋白H2A的K118/K119位点（sN2攻击机制）。H2AK119ub1不仅是转录抑制的直接信号，还作为PRC2重新结合和扩散的停靠位点——形成PRC2→H3K27me3→PRC1→H2AK119ub1→PRC2的正反馈循环，锁死基因沉默状态。

RING1/PRC1是TE调控领域最核心且被充分验证的因子之一。在胚胎干细胞中，PRC1（特别是variant PRC1-RYBP复合体）负责H2AK119ub在ERV和LINE-1元件上的沉积→招募PRC2→H3K27me3→形成双价（bivalent）或完全沉默的染色质状态。RING1/PRC1缺失导致ERV-MERVL和LINE-1在ESC和早期胚胎中的灾难性去抑制。但PubMed 213篇（>100, REJECTED）使RING1不符合本筛选的新颖性标准。RING1作为TE调控的"已知已知"（well-established），为评估其他候选蛋白是否落入PRC1功能轴提供了基准对照——任何低PubMed候选蛋白若具有RING域+PCGF/CBX样互作伙伴+核PcG体定位特征，可能代表未被描述的PRC1样TE沉默复合物。

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q06587
- Protein Atlas: https://www.proteinatlas.org/ENSG00000204227-RING1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=RING1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q06587
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000204227-RING1/subcellular

![](https://images.proteinatlas.org/8701/41_D10_1_red_green.jpg)
![](https://images.proteinatlas.org/8701/41_D10_2_red_green.jpg)
![](https://images.proteinatlas.org/8701/42_D10_1_red_green.jpg)
![](https://images.proteinatlas.org/8701/42_D10_2_red_green.jpg)
![](https://images.proteinatlas.org/8701/43_D10_1_red_green.jpg)
![](https://images.proteinatlas.org/8701/43_D10_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q06587-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q06587 |
| SMART | SM00184; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR032443;IPR043540;IPR001841;IPR013083;IPR017907; |
| Pfam | PF16207;PF13923; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000204227-RING1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| BCOR | Biogrid, Opencell | true |
| BMI1 | Intact, Biogrid | true |
| CBX6 | Intact, Biogrid, Bioplex | true |
| CBX7 | Intact, Biogrid, Bioplex | true |
| CBX8 | Intact, Biogrid | true |
| CSNK2B | Biogrid, Bioplex | true |
| DCAF7 | Biogrid, Bioplex | true |
| PCGF1 | Intact, Biogrid, Bioplex | true |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
