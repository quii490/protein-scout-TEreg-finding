---
type: protein-evaluation
gene: "THUMPD2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## THUMPD2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | THUMPD2 / C2orf8 |
| 蛋白名称 | U6 snRNA (guanine-N(2))-methyltransferase THUMPD2 |
| 蛋白大小 | 503 aa / 56.4 kDa |
| UniProt ID | Q9BTF0 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoplasm; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 503 aa / 56.4 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=5 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=75.0; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR000241, IPR029063, IPR004114; Pfam: PF02926, PF |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 8 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **141.5/180** | |
| **归一化总分** | | | **78.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Uncertain |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- nucleus (GO:0005634)
- tRNA methyltransferase complex (GO:0043527)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 5 |
| PubMed broad count | 8 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C2orf8 |

**关键文献**:
1. N 2-methylguanosine modifications on human tRNAs and snRNA U6 are important for cell proliferation, protein translation and pre-mRNA splicing.. *Nucleic acids research*. PMID: 37283053
2. RNA-binding protein THUMPD2 inhibits proliferation and promotes metastasis in epithelial ovarian cancer.. *Heliyon*. PMID: 39071668
3. THUMP domain containing 2 protein possibly induces resistance to cisplatin and 5-fluorouracil in in vitro human esophageal squamous cell carcinoma cells as revealed by transposon activation mutagenesis.. *The journal of gene medicine*. PMID: 31656051
4. Integrative RNA profiling of TBEV-infected neurons and astrocytes reveals potential pathogenic effectors.. *Computational and structural biotechnology journal*. PMID: 35685361
5. Human TRMT112-Methyltransferase Network Consists of Seven Partners Interacting with a Common Co-Factor.. *International journal of molecular sciences*. PMID: 34948388

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 75.0 |
| 高置信度残基 (pLDDT>90) 占比 | 55.5% |
| 置信残基 (pLDDT 70-90) 占比 | 10.9% |
| 中等置信 (pLDDT 50-70) 占比 | 5.2% |
| 低置信 (pLDDT<50) 占比 | 28.4% |
| 有序区域 (pLDDT>70) 占比 | 66.4% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 中等质量（pLDDT=75.0，有序区 66.4%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR000241, IPR029063, IPR004114; Pfam: PF02926, PF01170 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SOS1 | 0.732 | 0.000 | — |
| TRMT11 | 0.663 | 0.000 | — |
| TRMT1 | 0.630 | 0.209 | — |
| TRMT112 | 0.612 | 0.292 | — |
| NUS1 | 0.606 | 0.000 | — |
| DHDDS | 0.606 | 0.000 | — |
| PNPT1 | 0.598 | 0.000 | — |
| APMAP | 0.577 | 0.000 | — |
| QTRT2 | 0.561 | 0.000 | — |
| TRMT1L | 0.542 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| hdlbp.S | psi-mi:"MI:0029"(cosedimentation through density g | pubmed:20174651|imex:IM-17228 |
| SPDL1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| LACRT | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| NOP58 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| RALY | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| HNRNPCL2 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| M | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-27674|pubmed:33208464 |
| WFS1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32814053|imex:IM-28217| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 8
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 8 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=75.0 + PDB: 无 | pLDDT=75.0, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 8 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. THUMPD2 — U6 snRNA (guanine-N(2))-methyltransferase THUMPD2，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小503 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 5 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9BTF0
- Protein Atlas: https://www.proteinatlas.org/ENSG00000138050-THUMPD2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=THUMPD2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9BTF0
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
