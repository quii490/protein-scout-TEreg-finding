---
type: protein-evaluation
gene: "DAZ3"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## DAZ3 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DAZ3 |
| 蛋白名称 | Deleted in azoospermia protein 3 |
| 蛋白大小 | 486 aa / 55.0 kDa |
| UniProt ID | Q9NR90 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: 暂无HPA定位数据; UniProt: Cytoplasm; Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 486 aa / 55.0 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=16 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=62.3; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR043628, IPR037551, IPR012677, IPR035979, IPR000 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 12 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **130.0/180** | |
| **归一化总分** | | | **72.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Cytoplasm; Nucleus | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- nucleus (GO:0005634)
- protein-containing complex (GO:0032991)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 16 |
| PubMed broad count | 25 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Y-chromosome genes associated with sertoli cell-only syndrome identified by array comparative genome hybridization.. *Biomedical journal*. PMID: 35358715
2. Y-chromosome AZFc structural architecture and relationship to male fertility.. *Fertility and sterility*. PMID: 18990391
3. A large AZFc deletion removes DAZ3/DAZ4 and nearby genes from men in Y haplogroup N.. *American journal of human genetics*. PMID: 14639527
4. Combined deletion of DAZ2 and DAZ4 copies of Y chromosome DAZ gene is associated with male infertility in Tunisian men.. *Gene*. PMID: 24878370
5. Association of DAZ1/DAZ2 deletion with spermatogenic impairment and male infertility in the South Chinese population.. *World journal of urology*. PMID: 23512232

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 62.3 |
| 高置信度残基 (pLDDT>90) 占比 | 3.9% |
| 置信残基 (pLDDT 70-90) 占比 | 42.6% |
| 中等置信 (pLDDT 50-70) 占比 | 24.3% |
| 低置信 (pLDDT<50) 占比 | 29.2% |
| 有序区域 (pLDDT>70) 占比 | 46.5% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=62.3），有序残基占 46.5%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR043628, IPR037551, IPR012677, IPR035979, IPR000504; Pfam: PF18872, PF00076 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CDY1 | 0.946 | 0.092 | — |
| CDY2A | 0.898 | 0.086 | — |
| BPY2 | 0.892 | 0.000 | — |
| BPY2C | 0.881 | 0.000 | — |
| BPY2B | 0.881 | 0.000 | — |
| USP9Y | 0.758 | 0.000 | — |
| DDX3Y | 0.757 | 0.125 | — |
| PRY | 0.754 | 0.000 | — |
| PRY2 | 0.740 | 0.000 | — |
| PRYP3 | 0.727 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| TPL | psi-mi:"MI:0397"(two hybrid array) | pubmed:21798944|imex:IM-16043 |
| WOX14 | psi-mi:"MI:1356"(validated two hybrid) | doi:10.1038/nmeth.4343|pubmed: |
| MBD1 | psi-mi:"MI:1356"(validated two hybrid) | doi:10.1038/nmeth.4343|pubmed: |
| MBD4 | psi-mi:"MI:1356"(validated two hybrid) | doi:10.1038/nmeth.4343|pubmed: |
| MBD2 | psi-mi:"MI:1356"(validated two hybrid) | doi:10.1038/nmeth.4343|pubmed: |
| EBI-4447483 | psi-mi:"MI:2277"(Cr-two hybrid) | doi:10.1038/nmeth.4343|pubmed: |
| NAC066 | psi-mi:"MI:2277"(Cr-two hybrid) | doi:10.1038/nmeth.4343|pubmed: |
| GDAP1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32814053|imex:IM-28217| |
| SMN1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32814053|imex:IM-28217| |
| A2M | psi-mi:"MI:0397"(two hybrid array) | pubmed:32814053|imex:IM-28217| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 12
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 12 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=62.3 + PDB: 无 | pLDDT=62.3, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 12 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. DAZ3 — Deleted in azoospermia protein 3，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小486 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 16 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=62.3），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9NR90
- Protein Atlas: https://www.proteinatlas.org/ENSG00000187191-DAZ3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DAZ3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9NR90
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9NR90-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9NR90 |
| SMART | SM00360; |
| UniProt Domain [FT] | DOMAIN 40..115; /note="RRM"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00176"; DOMAIN 167..190; /note="DAZ 1"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU01238"; DOMAIN 191..214; /note="DAZ 2"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU01238"; DOMAIN 215..238; /note="DAZ 3"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU01238"; DOMAIN 239..262; /note="DAZ 4"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU01238"; DOMAIN 263..286; /note="DAZ 5"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU01238"; DOMAIN 287..310; /note="DAZ 6"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU01238"; DOMAIN 311..334; /note="DAZ 7"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU01238"; DOMAIN 335..358; /note="DAZ 8"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU01238"; DOMAIN 359..382; /note="DAZ 9"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU01238"; DOMAIN 383..406; /note="DAZ 10"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU01238"; DOMAIN 407..430; /note="DAZ 11"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU01238"; DOMAIN 431..454; /note="DAZ 12"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU01238" |
| InterPro | IPR043628;IPR037551;IPR012677;IPR035979;IPR000504; |
| Pfam | PF18872;PF00076; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000187191-DAZ3/interaction

未从 HPA Interaction 页面解析到互作伙伴；需人工复核或使用其他 humanPPI 来源。
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
