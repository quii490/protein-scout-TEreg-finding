---
type: protein-evaluation
gene: "ZBP1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## ZBP1 — REJECTED (研究热度过高 (PubMed strict=535，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | ZBP1 / C20orf183, DLM1 |
| 蛋白名称 | Z-DNA-binding protein 1 |
| 蛋白大小 | 429 aa / 46.3 kDa |
| UniProt ID | Q9H171 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: 暂无HPA定位数据; UniProt: Cytoplasm; Nucleus; Cytoplasm; Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 429 aa / 46.3 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=535 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=52.9; PDB: 2L4M, 2LNB, 3EYI, 4KA4, 9J89 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR025735, IPR036388, IPR036390, IPR042371, IPR042 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **81.5/180** | |
| **归一化总分** | | | **45.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Cytoplasm; Nucleus; Cytoplasm; Nucleus | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 535 |
| PubMed broad count | 826 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C20orf183, DLM1 |

**关键文献**:
1. ZBP1 senses Brucella abortus DNA triggering type I interferon signaling pathway and unfolded protein response activation.. *Frontiers in immunology*. PMID: 39850894
2. Influenza Virus Z-RNAs Induce ZBP1-Mediated Necroptosis.. *Cell*. PMID: 32200799
3. AIM2 forms a complex with pyrin and ZBP1 to drive PANoptosis and host defence.. *Nature*. PMID: 34471287
4. ADAR1 restricts ZBP1-mediated immune response and PANoptosis to promote tumorigenesis.. *Cell reports*. PMID: 34686350
5. Cooperative sensing of mitochondrial DNA by ZBP1 and cGAS promotes cardiotoxicity.. *Cell*. PMID: 37352855

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 52.9 |
| 高置信度残基 (pLDDT>90) 占比 | 12.8% |
| 置信残基 (pLDDT 70-90) 占比 | 14.7% |
| 中等置信 (pLDDT 50-70) 占比 | 9.1% |
| 低置信 (pLDDT<50) 占比 | 63.4% |
| 有序区域 (pLDDT>70) 占比 | 27.5% |
| 可用 PDB 条目 | 2L4M, 2LNB, 3EYI, 4KA4, 9J89 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=52.9），有序残基占 27.5%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR025735, IPR036388, IPR036390, IPR042371, IPR042361; Pfam: PF12721, PF02295 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| RIPK1 | 0.998 | 0.626 | — |
| RIPK3 | 0.996 | 0.292 | — |
| IRF3 | 0.989 | 0.095 | — |
| TBK1 | 0.986 | 0.095 | — |
| IRF7 | 0.977 | 0.065 | — |
| IKBKE | 0.963 | 0.091 | — |
| CASP8 | 0.823 | 0.000 | — |
| ADAR | 0.751 | 0.000 | — |
| MLKL | 0.720 | 0.000 | — |
| MEFV | 0.708 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| LYAR | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| FTSJ1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| SMYD2 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| PUF60 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| ILK | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| HLA-B | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| CNBP | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| PRKRA | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| IKBKE | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| ARHGDIA | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=52.9 + PDB: 2L4M, 2LNB, 3EYI, 4KA4, 9J89 | pLDDT=52.9, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus; Cytoplasm; Nucleus / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. ZBP1 — Z-DNA-binding protein 1，研究基础较多，新颖性有限。
2. 蛋白大小429 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 535 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=52.9），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 535 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9H171
- Protein Atlas: https://www.proteinatlas.org/ENSG00000124256-ZBP1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=ZBP1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9H171
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
