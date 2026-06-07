---
type: protein-evaluation
gene: "MSGN1"
date: 2026-01-30
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## MSGN1 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 | MSGN1 |
| 别名 | pMesogenin1 |
| 基因全称 | mesogenin 1 |
| 蛋白名称 | Mesogenin-1 |
| 蛋白大小 | 193 aa |
| UniProt ID | A6NI15 |
| 评估日期 | 2026-01-30 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| Nucleus 核定位特异性 | 4/10 | x4 | 16 | HPA: Nuclear bodies |
| Size 蛋白大小 | 8/10 | x1 | 8 | 193 aa |
| Novelty 研究新颖性 | 8/10 | x5 | 40 | PubMed: 24 篇 |
| 3D Structure 三维结构 | 7/10 | x3 | 21 | AlphaFold pLDDT=66.3 |
| Domain 调控结构域 | 7/10 | x2 | 14 | 含 bHLH 结构域，转录因子 |
| PPI Network PPI网络 | 4/10 | x3 | 12 | STRING+IntAct+GO-CC |
| Cross-validation 互证加分 | — | max +3 | +0.5 | — |
| **原始总分** |  |  | **111.5/183** |  |
| **归一化总分** |  |  | **60.9/100** |  |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Sperm | HPA validated |
| UniProt |  | — |
| GO-CC | GO:0005634 Nucleus (IEA|IMP) | — |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/MSGN1/IF_images/Sperm_1.jpg|Sperm]]
#### 3.2 蛋白大小评估

193 aa，小型蛋白，实验操作便利

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 24 篇 |
| 最早发表年份 | 2025 |

**主要研究方向**:
- 功能研究尚不充分，属新颖蛋白

**关键文献**:
1. Braccioli L et al. (2025). "Identifying cross-lineage dependencies of cell-type-specific regulators in mouse gastruloids.". *Dev Cell*. PMID: 40101716
2. Chalamalasetty RB et al. (2011). "The Wnt3a/β-catenin target gene Mesogenin1 controls the segmentation clock by activating a Notch signalling program.". *Nat Commun*. PMID: 21750544
3. Chalamalasetty RB et al. (2014). "Mesogenin 1 is a master regulator of paraxial presomitic mesoderm differentiation.". *Development*. PMID: 25371364
4. Fior R et al. (2012). "The differentiation and movement of presomitic mesoderm progenitor cells are controlled by Mesogenin 1.". *Development*. PMID: 23172917
5. Yabe T et al. (2012). "Mesogenin causes embryonic mesoderm progenitors to differentiate during development of zebrafish tail somites.". *Dev Biol*. PMID: 22890044


**评价**: PubMed 24 篇，属非常新颖蛋白，研究空间充足。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 平均 pLDDT | 66.3 |
| pLDDT > 90 占比 | 29.0% |
| pLDDT 70-90 占比 | 5.7% |
| pLDDT 50-70 占比 | 39.4% |
| pLDDT < 50 占比 | 25.9% |
| 可用 PDB 条目 | 0 |

**PAE 图**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/MSGN1/MSGN1-PAE.png]]

**评价**: AlphaFold 预测中等质量，部分区域有序 (AlphaFold v6, pLDDT=66.3, >90=29%, 70-90=6%, 50-70=39%, <50=26%)

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| UniProt | — |

**染色质调控潜力分析**: 含 bHLH 结构域，转录因子

#### 3.6 PPI 网络

**实验验证互作** (IntAct, physical association):

| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---------|------|------|---------|-----------|
| intact:EBI-11991020|ensembl:ENSP00000281047.3 | MI:0397(two hybrid array) | PMID:pubmed:32296183|imex:IM-25472 | — | — |
| - | MI:1356(validated two hybrid) | PMID:pubmed:32296183|imex:IM-25472 | — | — |
|

**STRING 预测互作** (combined score >0.4):

| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|-----------|
| TBX6 | 0.0 | — | — |
| TCF4 | 0.0 | — | — |
| ID4 | 0.0 | — | — |
| RBPJ | 0.0 | — | — |
| CTNNB1 | 0.0 | — | — |
| MEOX1 | 0.0 | — | — |
| LEF1 | 0.0 | — | — |
| RIPPLY2 | 0.0 | — | — |
|

**已知复合体成员** (GO Cellular Component):
- 暂无 GO-CC 复合体注释


**PPI 互证分析**:
- STRING + IntAct 共同确认: 0
- 仅 STRING 预测: 15
- 仅 IntAct 实验: 2
- 调控相关比例: 2/15 (13%)

**评价**: PPI 得分 4/10。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold + PDB | pLDDT=66.3, PDB=0 | — |
| 结构域 | UniProt/InterPro | 无注释域 | — |
| PPI | STRING + IntAct + GO-CC | 15/2/0 条目 | — |
| 定位 | HPA/UniProt/GO | Nuclear bodies / Nucleus / GO:0005634 | 一致 |

**互证加分明细**:
- IntAct+STRING 双源确认 (+0.5)
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: ★★ (3/5)

**核心优势**:
1. 非常新颖 (PubMed 24 篇)，几乎未被研究
2. HPA 确认核定位，中等置信度

**风险/不确定性**:
1. AlphaFold 预测质量中等 (pLDDT=66.3)，部分区域无序
2. PPI 数据丰富，功能网络尚不清晰

**下一步建议**:
- [ ] 通过 IF 实验验证内源核定位
- [ ] 构建表达载体进行功能研究
- [ ] Co-IP/MS 鉴定互作蛋白

### 5. 数据来源
- GeneCards: https://www.genecards.org/cgi-bin/carddisp.pl?gene=MSGN1
- Protein Atlas: https://www.proteinatlas.org/MSGN1
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=MSGN1
- UniProt: https://www.uniprot.org/uniprotkb/A6NI15
- SMART: http://smart.embl.de/
- STRING: https://string-db.org/
- IntAct: https://www.ebi.ac.uk/intact/
- AlphaFold: https://alphafold.ebi.ac.uk/entry/A6NI15


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[MSGN1-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/MSGN1/MSGN1-PAE.png]]

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | A6NI15 |
| SMART | SM00353; |
| UniProt Domain [FT] | DOMAIN 124..178; /note="bHLH"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00981" |
| InterPro | IPR011598;IPR036638;IPR040259; |
| Pfam | PF00010; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000151379-MSGN1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| BRAT1 | Intact | false |
| CCDC172 | Intact | false |
| CTAG1A | Intact | false |
| CTAG1B | Intact | false |
| DNALI1 | Intact | false |
| HAP1 | Intact | false |
| ID1 | Intact | false |
| ID2 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
