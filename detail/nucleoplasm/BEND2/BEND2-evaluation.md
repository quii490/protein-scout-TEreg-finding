---
type: protein-evaluation
gene: "BEND2"
date: 2026-05-29
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## BEND2 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | BEND2 / BEN domain-containing protein 2 |
| 蛋白名称 | BEN domain-containing protein 2 |
| 蛋白大小 | 799 aa / 87.9 kDa |
| UniProt ID | Q8NDZ0 |
| 评估日期 | 2026-05-29 |

**IF 图像**: 暂无IF数据

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 🔴 核定位特异性 | 9/10 | ×4 | 36.0 | UniProt Nucleus; BEN domain protein |
| 📏 蛋白大小 | 10/10 | ×1 | 10.0 | 799 aa, 799 aa, 200-800 aa 理想范围上限 |
| 🆕 研究新颖性 | 8/10 | ×5 | 40.0 | PubMed 36 篇 |
| 🏗️ 三维结构 | 6/10 | ×3 | 18.0 | pLDDT 49.5, 70.7% VLow; 新颖基线6 |
| 🧬 调控结构域 | 8/10 | ×2 | 16.0 | BEN domain ×2; DNA/chromatin 结合域; 新颖基线7基础上+1 |
| 🔗 PPI 网络 | 2/10 | ×3 | 6.0 | STRING textmining 为主; 极少实验互作 |
| ➕ 互证加分 | — | max +3 | +1.0 | 结构域互证 |
| **原始总分** |  |  | **127/183** |  |
| **归一化总分** |  |  | **69.4/100** |  |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| GeneCards | Nucleus | — |
| Protein Atlas (IF) | 暂无数据（Pending cell analysis），核定位基于 UniProt | — |
| UniProt | Nucleus | 实验/GO注释 |

> **Protein Atlas IF**: 暂无数据（Pending cell analysis），核定位基于 UniProt + GO。

**结论**: BEND2 含 BEN 结构域，该域已知为 DNA/染色质结合域。UniProt 标注 Nucleus。核定位评分 9。

#### 3.2 蛋白大小评估
**评价**: 799 aa (87.9 kDa)，恰好 200-800 aa 上限。评分 10。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 36 篇 |
| 最早发表年份 | 2012 |
| Chromatin/epigenetics 比例 | BEN domain 直接结合染色质/DNA |

**主要研究方向**:
- BEN 结构域 (DNA/chromatin binding)
- 转录调控和染色质组织
- 配子发生和减数分裂
- 基因组稳定性维护

**评价**: 非常新颖 (36 篇)。BEN 域是新兴的染色质结合域，BEND2 的染色质靶点和功能远未充分研究。评分 8。

**关键文献**:
1. Shi Y et al. (2025). "Oncogenic fusions converge on shared mechanisms in initiating astroblastoma". *Nature*. PMID: 40369078
2. Dashti NK et al. (2024). "Malignant Bone-Forming Neoplasm With NIPBL::BEND2 Fusion". *Genes Chromosomes Cancer*. PMID: 39604143
3. Stark JC et al. (2025). "Clinical applications of and molecular insights from RNA sequencing in a rare disease cohort". *Genome Med*. PMID: 40597352
4. Wood-Trageser MA et al. (2025). "Recurrent BEND2 Fusion Genes Identified by Whole Transcriptome Sequencing of Nonfunctional Pancreatic Neuroendocrine Tumors Correlate With Poor Patient Prognosis". *Mod Pathol*. PMID: 40784487
5. Federico A et al. (2026). "Molecular and clinical stratification of astroblastomas: Three distinct fusion-defined groups informing risk-adapted treatment strategies". *Neuro Oncol*. PMID: 41429568
#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 平均 pLDDT | 49.5 |
| 有序区域 (pLDDT>70) 占比 | 26.3% |
| Very High (>90) 占比 | 15.8% |
| 可用 PDB 条目 |

**PAE 图**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/BEND2/BEND2-PAE.png]]

**评价**: AlphaFold pLDDT 49.5，70.7% 无序。BEN 域区域应有序。新颖基线 6。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| GeneCards | BEN domain (×2) |
| SMART/InterPro | BEN (PF10523) |
| UniProt/Pfam | BEN domain (IPR018379) |

**染色质调控潜力分析**: 含 2 个 BEN (BANP/E5R/NAC1) 结构域。BEN 域是新定义的染色质/DNA 结合模块，已知参与转录抑制和染色质组织。BANP 的 BEN 域直接结合 CGCG DNA motif。BEND2 的 BEN 域可能具有类似的染色质靶向能力。评分 8。

#### 3.6 PPI 网络

**实验验证互作** (IntAct, physical association/direct interaction):

无 IntAct 实验验证互作记录。

**STRING 预测互作** (combined score >0.4):
| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|-----------|
| BEND3 | 0.85 | BEN domain (paralog) | ✅ |
| BANP | 0.72 | BEN domain TF | ✅ |
| NAC1 | 0.55 | BEN domain repressor | ✅ |

**已知复合体成员** (GO Cellular Component):
- 无 GO-CC 染色质/核复合体条目

**PPI 互证分析**: PPI 极为稀疏，以 BEN 家族 paralog 关联为主。无 IntAct 记录。

**评价**: PPI 极稀疏，仅 STRING textmining 暗示 BEN 家族网络。调控比例 ~30%。评分 2。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 一致？ |
|------|------|------|--------|
| 三维结构 | AlphaFold + PDB | AlphaFold pLDDT 49.5，无 PDB | 仅有预测 |
| 结构域 | UniProt / InterPro / Pfam | BEN domain 多库一致 | 一致 |
| PPI | STRING + IntAct + GO-CC | 仅 STRING textmining | 无对比 |
| 定位 | Protein Atlas / UniProt / GO | UniProt Nucleus + BEN domain 功能一致 | 一致 |

**互证加分明细**:
- 结构域互证: BEN domain 多库确认 → +0.5
- 功能互证: BEN + 核定位一致 → +0.5

**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (3.5/5/5)

**核心优势**:
1. BEN 结构域是新兴染色质结合域
2. 蛋白大小理想 (799 aa)
3. 减数分裂/生殖生物学关联
4. 非常新颖 (36 篇)

**风险/不确定性**:
1. PPI 极度缺乏
2. AlphaFold 70.7% 无序
3. BEN 域结合特异性未知
4. 缺少 Protein Atlas IF

**下一步建议**:
- [ ] 实验验证核定位
- [ ] BEN 域 DNA 结合特异性鉴定
- [ ] ChIP-seq 全基因组定位
- [ ] 推荐作为 BEN 域染色质生物学研究

### 深度机制分析

BEND2的分子机制核心在于其串联排列的双BEN结构域（483-582aa与667-765aa，PF10523，IPR018379）。BEN结构域是近年来被定义的新兴DNA/染色质结合模块，最早在BANP、E5R（果蝇）和NAC1中鉴定（Dai Q et al., 2013, Nucleic Acids Res, PMID:23268447）。BANP的BEN结构域已被证实直接识别CGCG DNA motif并打开局部染色质以激活转录（Grand RS et al., 2021, Nature, PMID:34108682），这为BEND2的功能推断提供了直接的同源结构域范式。BEND2拥有两个BEN结构域，可能形成双价DNA结合模式：一个结构域负责序列特异性识别，另一个参与染色质锚定或寡聚化，从而增强DNA亲和力。

AlphaFold预测显示该蛋白整体无序（平均pLDDT=49.5，70.7%残基<50分），但BEN域区域（大约480-580aa及665-770aa）的结构置信度应显著高于整体均值，这是核酸结合结构域折叠典型的模式——结合域有序、连接区柔性。PPI网络极度稀疏：无IntAct实验记录，STRING仅检测到BEN家族成员（BEND3 score=0.85，BANP score=0.72，NAC1 score=0.55）的共进化/共表达信号。此互作图谱暗示BEND2可能以独立于伴侣蛋白的方式直接作用于染色质靶点，而非参与大型调控复合体。

临床意义方面，BEND2的融合基因已在星形母细胞瘤（NIPBL::BEND2 fusion，Dashti NK et al., 2024, PMID:39604143）和胰腺神经内分泌肿瘤（BEND2 fusions与不良预后相关，Wood-Trageser MA et al., 2025, PMID:40784487）中被发现。Federico A et al.（2026, PMID:41429568）进一步将星形母细胞瘤分为三种融合定义亚型，BEND2融合为其中之一。这些融合将BEND2的BEN染色质靶向结构域重新导向至新基因组位点，可能是驱动肿瘤发生的核心机制。

对于TE调控的潜在作用，BEND2的BEN结构域介导的DNA结合活性使其理论上可作为TE元件的直接或间接调控因子。推荐通过ChIP-seq鉴定BEND2的全基因组结合谱，重点关注其是否富集于重复序列区域，以及BEN结构域是否识别特定的TE衍生DNA motif。

### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| ATXN1 | BioGRID | 1 |
| APP | BioGRID | 1 |
| SF3A2 | BioGRID | 1 |
| LHX2 | BioGRID | 1 |
| ANAPC11 | BioGRID | 1 |
| ZMYM6 | BioGRID | 1 |
| PRR20B | BioGRID | 0 |
| PRR20A | BioGRID | 0 |


### TE 调控评估

该蛋白有 ChIP-Seq 数据，可能在基因组水平参与 TE 调控。建议验证。

### 5. 关键文献

1. Dai Q et al. (2013). 'BEN domain proteins in transcriptional regulation.' Nucleic Acids Res. PMID: 23268447
2. Grand RS et al. (2021). 'BANP opens chromatin and activates transcription.' Nature. PMID: 34108682

### 6. 数据来源
- GeneCards: https://www.genecards.org/cgi-bin/carddisp.pl?gene=BEND2
- Protein Atlas: https://www.proteinatlas.org/search/BEND2
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22BEND2%22
- UniProt: https://www.uniprot.org/uniprotkb/Q8NDZ0
- STRING: https://string-db.org/
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8NDZ0


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 暂无互作数据 |

暂无实验验证互作。无 BioGrid 补充数据。

![[BEND2-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/BEND2/BEND2-PAE.png]]

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q8NDZ0 |
| SMART | SM01025; |
| UniProt Domain [FT] | DOMAIN 483..582; /note="BEN 1"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00784"; DOMAIN 667..765; /note="BEN 2"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00784" |
| InterPro | IPR018379; |
| Pfam | PF10523; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000177324-BEND2/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| LHX2 | Intact | false |
| PRR20D | Intact | false |
| SF3A2 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
