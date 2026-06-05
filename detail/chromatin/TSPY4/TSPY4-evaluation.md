---
type: protein-evaluation
gene: "TSPY4"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## TSPY4 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | TSPY4 |
| 蛋白名称 | Testis-specific Y-encoded protein 4 |
| 蛋白大小 | 314 aa / 35.7 kDa |
| UniProt ID | P0CV99 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Cytosol; UniProt: Cytoplasm; Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 314 aa / 35.7 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=6 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=71.7; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR037231, IPR002164; Pfam: PF00956 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **133.0/180** | |
| **归一化总分** | | | **73.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol | Approved |
| UniProt | Cytoplasm; Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- chromatin (GO:0000785)
- cytoplasm (GO:0005737)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 6 |
| PubMed broad count | 9 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Comprehensive Analysis of Juvenile Nasopharyngeal Angiofibromas via Whole-Exome Sequencing.. *Genes, chromosomes & cancer*. PMID: 39297564
2. Transcriptome analyses in infertile men reveal germ cell-specific expression and splicing patterns.. *Life science alliance*. PMID: 36446526
3. Assessment of the vaginal residence time of biomarkers of semen exposure.. *Contraception*. PMID: 27259675
4. TSPY4 is a novel sperm-specific biomarker of semen exposure in human cervicovaginal fluids; potential use in HIV prevention and contraception studies.. *Contraception*. PMID: 23312930
5. Development of a composite measure of product adherence, protocol compliance, and semen exposure using DNA and protein biomarkers for topical HIV prevention studies.. *PloS one*. PMID: 25489736

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 71.7 |
| 高置信度残基 (pLDDT>90) 占比 | 41.4% |
| 置信残基 (pLDDT 70-90) 占比 | 15.9% |
| 中等置信 (pLDDT 50-70) 占比 | 12.1% |
| 低置信 (pLDDT<50) 占比 | 30.6% |
| 有序区域 (pLDDT>70) 占比 | 57.3% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=71.7，有序区 57.3%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR037231, IPR002164; Pfam: PF00956 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| RBMY1B | 0.721 | 0.049 | — |
| RBMY1E | 0.592 | 0.049 | — |
| RBMY1J | 0.588 | 0.049 | — |
| TGIF2LY | 0.581 | 0.000 | — |
| RPS4Y2 | 0.547 | 0.000 | — |
| RBMY1F | 0.517 | 0.049 | — |
| AMELY | 0.481 | 0.000 | — |
| EIF1AY | 0.478 | 0.000 | — |
| CCDC89 | 0.476 | 0.000 | — |
| HSFY2 | 0.475 | 0.000 | — |

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
| 三维结构 | AlphaFold pLDDT=71.7 + PDB: 无 | pLDDT=71.7, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus / Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. TSPY4 — Testis-specific Y-encoded protein 4，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小314 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 6 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P0CV99
- Protein Atlas: https://www.proteinatlas.org/ENSG00000233803-TSPY4/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TSPY4
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P0CV99
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Cytosol (approved)。来源: https://www.proteinatlas.org/ENSG00000233803-TSPY4/subcellular

![](https://images.proteinatlas.org/49384/1819_E1_20_cr59f6e24d75cdb_blue_red_green.jpg)
![](https://images.proteinatlas.org/49384/1819_E1_4_cr59f6e24d76ce2_blue_red_green.jpg)
![](https://images.proteinatlas.org/49384/1833_B11_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/49384/1833_B11_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/49384/1864_G8_14_cr5afd99d66e2e4_blue_red_green.jpg)
![](https://images.proteinatlas.org/49384/1864_G8_29_cr5afd99d66e2e8_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P0CV99-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
