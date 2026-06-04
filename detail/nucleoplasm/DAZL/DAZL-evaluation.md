---
type: protein-evaluation
gene: "DAZL"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## DAZL — REJECTED (研究热度过高 (PubMed strict=445，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DAZL / DAZH, DAZL1, DAZLA, SPGYLA |
| 蛋白名称 | Deleted in azoospermia-like |
| 蛋白大小 | 295 aa / 33.2 kDa |
| UniProt ID | Q92904 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: 暂无HPA定位数据; UniProt: Cytoplasm; Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 295 aa / 33.2 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=445 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=57.4; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR043628, IPR037551, IPR012677, IPR035979, IPR000 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 10 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **80.0/180** | |
| **归一化总分** | | | **44.4/100** | |

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
- ribosome (GO:0005840)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 445 |
| PubMed broad count | 699 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: DAZH, DAZL1, DAZLA, SPGYLA |

**关键文献**:
1. A genome-wide screen reveals new regulators of the 2-cell-like cell state.. *Nature structural & molecular biology*. PMID: 37488355
2. Gene expression patterns and protein cellular localization suggest a novel role for DAZL in developing Tibetan sheep testes.. *Gene*. PMID: 31927007
3. Association of DAZL polymorphisms and DAZ deletion with male infertility: a systematic review and meta-analysis.. *Genes & genomics*. PMID: 36434389
4. The roles of DAZL in RNA biology and development.. *Wiley interdisciplinary reviews. RNA*. PMID: 24715697
5. The retrotransposon-derived capsid genes PNMA1 and PNMA4 maintain reproductive capacity.. *Nature aging*. PMID: 40263616

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 57.4 |
| 高置信度残基 (pLDDT>90) 占比 | 23.7% |
| 置信残基 (pLDDT 70-90) 占比 | 4.7% |
| 中等置信 (pLDDT 50-70) 占比 | 15.3% |
| 低置信 (pLDDT<50) 占比 | 56.3% |
| 有序区域 (pLDDT>70) 占比 | 28.4% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=57.4），有序残基占 28.4%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR043628, IPR037551, IPR012677, IPR035979, IPR000504; Pfam: PF18872, PF00076 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| PUM2 | 0.993 | 0.617 | — |
| DAZAP2 | 0.935 | 0.292 | — |
| DDX4 | 0.922 | 0.125 | — |
| SYCE1 | 0.883 | 0.000 | — |
| SYCE2 | 0.871 | 0.000 | — |
| NANOS3 | 0.861 | 0.093 | — |
| STRA8 | 0.851 | 0.000 | — |
| SYCP1 | 0.840 | 0.073 | — |
| DAZAP1 | 0.839 | 0.456 | — |
| PRDM14 | 0.817 | 0.054 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| HSPD1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| PXN | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| EEF1A2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| NCBP1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| ELAVL2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| TRAF3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| ELAVL3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| WDR83 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| POTEKP | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| PAIP1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 10
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 10 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=57.4 + PDB: 无 | pLDDT=57.4, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 10 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. DAZL — Deleted in azoospermia-like，研究基础较多，新颖性有限。
2. 蛋白大小295 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 445 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=57.4），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 445 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q92904
- Protein Atlas: https://www.proteinatlas.org/ENSG00000092345-DAZL/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DAZL
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q92904
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
