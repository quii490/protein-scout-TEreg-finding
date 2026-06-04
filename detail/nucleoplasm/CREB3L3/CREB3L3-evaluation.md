---
type: protein-evaluation
gene: "CREB3L3"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## CREB3L3 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CREB3L3 / CREBH |
| 蛋白名称 | Cyclic AMP-responsive element-binding protein 3-like protein 3 |
| 蛋白大小 | 461 aa / 49.1 kDa |
| UniProt ID | Q68CJ9 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: 暂无HPA定位数据; UniProt: Endoplasmic reticulum membrane; Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 461 aa / 49.1 kDa |
| 研究新颖性 | 4/10 | ×5 | 20 | PubMed strict=71 篇 (≤80→4) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=58.9; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR004827, IPR046347, IPR051381; Pfam: PF00170 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **100.0/180** | |
| **归一化总分** | | | **55.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Endoplasmic reticulum membrane; Nucleus | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- chromatin (GO:0000785)
- cytosol (GO:0005829)
- endoplasmic reticulum (GO:0005783)
- endoplasmic reticulum membrane (GO:0005789)
- Golgi membrane (GO:0000139)
- membrane (GO:0016020)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 71 |
| PubMed broad count | 154 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: CREBH |

**关键文献**:
1. Mechanisms of hepatic fatty acid oxidation and ketogenesis during fasting.. *Trends in endocrinology and metabolism: TEM*. PMID: 37940485
2. Sclerosing Epithelioid Fibrosarcoma.. *Surgical pathology clinics*. PMID: 38278601
3. Creb3l3 deficiency promotes intestinal lipid accumulation and alters ApoB-containing lipoprotein kinetics.. *Journal of lipid research*. PMID: 40449732
4. Hepatic CREB3L3 controls whole-body energy homeostasis and improves obesity and diabetes.. *Endocrinology*. PMID: 25233440
5. Hyperlipidemia and hepatitis in liver-specific CREB3L3 knockout mice generated using a one-step CRISPR/Cas9 system.. *Scientific reports*. PMID: 27291420

**评价**: 已有一定研究基础，但仍存在niche空间。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 58.9 |
| 高置信度残基 (pLDDT>90) 占比 | 15.6% |
| 置信残基 (pLDDT 70-90) 占比 | 15.2% |
| 中等置信 (pLDDT 50-70) 占比 | 16.5% |
| 低置信 (pLDDT<50) 占比 | 52.7% |
| 有序区域 (pLDDT>70) 占比 | 30.8% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=58.9），有序残基占 30.8%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR004827, IPR046347, IPR051381; Pfam: PF00170 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CREB1 | 0.972 | 0.284 | — |
| CREB3 | 0.958 | 0.513 | — |
| MBTPS2 | 0.953 | 0.000 | — |
| CREB3L1 | 0.950 | 0.345 | — |
| PPARGC1A | 0.950 | 0.292 | — |
| MBTPS1 | 0.945 | 0.000 | — |
| CRTC2 | 0.942 | 0.000 | — |
| CREB3L2 | 0.940 | 0.199 | — |
| GSK3B | 0.935 | 0.292 | — |
| ATF4 | 0.935 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| USP7 | psi-mi:"MI:0018"(two hybrid) | pubmed:16713569|imex:IM-11827| |
| PELI2 | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |
| KHDRBS1 | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |
| BAD | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| RIOK3 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| KPNA2 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| ATF6 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:16469704|imex:IM-11834 |
| FATE1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| SGTA | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| RUSF1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=58.9 + PDB: 无 | pLDDT=58.9, v6 | 仅预测 |
| 定位 | UniProt + HPA | Endoplasmic reticulum membrane; Nucleus / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. CREB3L3 — Cyclic AMP-responsive element-binding protein 3-like protein 3，已有一定研究基础，但仍存在niche空间。
2. 蛋白大小461 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 71 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=58.9），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q68CJ9
- Protein Atlas: https://www.proteinatlas.org/ENSG00000060566-CREB3L3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CREB3L3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q68CJ9
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
