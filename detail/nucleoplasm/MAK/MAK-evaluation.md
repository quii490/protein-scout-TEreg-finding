---
type: protein-evaluation
gene: "MAK"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## MAK — REJECTED (研究热度过高 (PubMed strict=250，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | MAK |
| 蛋白名称 | Serine/threonine-protein kinase MAK |
| 蛋白大小 | 623 aa / 70.6 kDa |
| UniProt ID | P20794 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Basal body, Cytosol, Connecting piece; 额外: Nucl; UniProt: Nucleus; Cytoplasm, cytoskeleton, microtubule organizing cen |
| 蛋白大小 | 10/10 | ×1 | 10 | 623 aa / 70.6 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=250 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=62.1; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR011009, IPR050117, IPR000719, IPR017441, IPR008 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 0.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **79.5/180** | |
| **归一化总分** | | | **44.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Basal body, Cytosol, Connecting piece; 额外: Nucleoli, Plasma membrane, Principal piece, End piece | Approved |
| UniProt | Nucleus; Cytoplasm, cytoskeleton, microtubule organizing center, centrosome; Cytoplasm, cytoskeleton... | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- axoneme (GO:0005930)
- centrosome (GO:0005813)
- ciliary basal body (GO:0036064)
- cilium (GO:0005929)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- midbody (GO:0030496)
- mitotic spindle (GO:0072686)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 250 |
| PubMed broad count | 17115 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Nonsyndromic Retinitis Pigmentosa Overview.. **. PMID: 20301590
2. Regulation of Chondrocyte Metabolism and Osteoarthritis Development by Sirt5 Through Protein Lysine Malonylation.. *Arthritis & rheumatology (Hoboken, N.J.)*. PMID: 40176311
3. Chlamydomonas protein kinase MAK phosphorylates FAP256/CEP104 and regulates axonemal microtubule assembly.. *Proceedings of the National Academy of Sciences of the United States of America*. PMID: 41231942
4. MAPK/MAK/MRK overlapping kinase (MOK) controls microglial inflammatory/type-I IFN responses via Brd4 and is involved in ALS.. *Proceedings of the National Academy of Sciences of the United States of America*. PMID: 37399380
5. Ccrk-Mak/Ick signaling is a ciliary transport regulator essential for retinal photoreceptor survival.. *Life science alliance*. PMID: 39293864

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 62.1 |
| 高置信度残基 (pLDDT>90) 占比 | 35.5% |
| 置信残基 (pLDDT 70-90) 占比 | 8.7% |
| 中等置信 (pLDDT 50-70) 占比 | 3.9% |
| 低置信 (pLDDT<50) 占比 | 52.0% |
| 有序区域 (pLDDT>70) 占比 | 44.2% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=62.1），有序残基占 44.2%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011009, IPR050117, IPR000719, IPR017441, IPR008271; Pfam: PF00069 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| MCM3 | 0.801 | 0.801 | — |
| CDC6 | 0.787 | 0.782 | — |
| MCM2 | 0.787 | 0.782 | — |
| ORC4 | 0.783 | 0.782 | — |
| ORC3 | 0.783 | 0.782 | — |
| MCM7 | 0.782 | 0.782 | — |
| MCM6 | 0.782 | 0.782 | — |
| ORC2 | 0.782 | 0.782 | — |
| CDT1 | 0.782 | 0.782 | — |
| MCM5 | 0.782 | 0.782 | — |

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
| 三维结构 | AlphaFold pLDDT=62.1 + PDB: 无 | pLDDT=62.1, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm, cytoskeleton, microtubule orga / Nucleoplasm, Basal body, Cytosol, Connecting piece | 一致 |
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
1. MAK — Serine/threonine-protein kinase MAK，研究基础较多，新颖性有限。
2. 蛋白大小623 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 250 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=62.1），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 250 > 100，研究热度过高，不符合novelty筛选标准。**

### 深度机制分析

MAK（Serine/threonine-protein kinase MAK, 623 aa, UniProt P20794）。定位于Nucleoplasm（HPA Supported），同时有Basal body/Centrosome/Cytosol等细胞骨架相关定位。属MAPK/MAK/MRK overlapping kinase家族，InterPro注释IPR011009（kinase-like domain superfamily）、IPR050117（MAK subfamily）、IPR000719（protein kinase domain）、IPR017441（protein kinase ATP binding site）、IPR008271（serine/threonine-protein kinase active site）。Pfam PF00069（Pkinase），SMART SM00220（S_TKc）。UniProt FT标注DOMAIN 4-284为Protein kinase域。AlphaFold pLDDT=62.1（有序区44.2%），无PDB实验结构。

从激酶结构域与信号通路角度，MAK的激酶结构域（4-284 aa）催化丝氨酸/苏氨酸磷酸化。STRING预测的互作伙伴几乎全为DNA复制许可因子——MCM3（0.801, experimental=0.801）、CDC6（0.787）、MCM2-MCM7（0.782-0.787）、ORC2-ORC4（0.782-0.783）、CDT1（0.782）——均为高置信度co-expression实验数据。这一模式极为异常：MAK是cilia/centrosome相关激酶（PMID:39293864, PMID:41231942），却与核DNA复制因子关联，提示非经典核功能。HPA interaction页面显示FZR1（泛素连接酶共激活因子，Intact+Biogrid）和AR（雄激素受体，Intact）实验互作。

从TE调控角度，MAK研究集中于纤毛发生和视网膜光感受器存活（PMID:20301590, PMID:39293864），PubMed=250篇文献中未检索到与TE/转座子调控直接相关的报道。然而，nucleoplasm定位和MCM/ORC复制起始复合体的关联提示可能参与S期染色质调控——TE的转录爆发常发生在S期复制叉通过富集TE的区域时。激酶活性可通过磷酸化染色质结合蛋白（如HP1、KAP1）调节异染色质稳定性。

但PubMed 250篇超出新颖性阈值（>100），不符合本筛查的优先研究目标标准。综合评分44.2/100。

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P20794
- Protein Atlas: https://www.proteinatlas.org/ENSG00000111837-MAK/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=MAK
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P20794
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000111837-MAK/subcellular

![](https://images.proteinatlas.org/77174/2053_E4_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/77174/2053_E4_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/77174/2058_B5_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/77174/2058_B5_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/77174/2059_F4_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/77174/2059_F4_4_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P20794-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | P20794 |
| SMART | SM00220; |
| UniProt Domain [FT] | DOMAIN 4..284; /note="Protein kinase"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00159" |
| InterPro | IPR011009;IPR050117;IPR000719;IPR017441;IPR008271; |
| Pfam | PF00069; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000111837-MAK/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| FZR1 | Intact, Biogrid | true |
| KATNIP | Intact, Biogrid | true |
| AR | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
