---
type: protein-evaluation
gene: "TCFL5"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## TCFL5 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | TCFL5 / CHA, E2BP1 |
| 蛋白名称 | Transcription factor-like 5 protein |
| 蛋白大小 | 500 aa / 52.7 kDa |
| UniProt ID | Q9UL49 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoplasm; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 500 aa / 52.7 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=27 篇 (≤40→8) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=53.1; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR011598, IPR036638, IPR039583; Pfam: PF00010 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 6 partners; IntAct 1 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **128.0/180** | |
| **归一化总分** | | | **71.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Supported |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- chromatin (GO:0000785)
- male germ cell nucleus (GO:0001673)
- nucleus (GO:0005634)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 27 |
| PubMed broad count | 36 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: CHA, E2BP1 |

**关键文献**:
1. The MYBL1/TCFL5 transcription network: two collaborative factors with central role in male meiosis.. *Biochemical Society transactions*. PMID: 38015556
2. The transcription factor TCFL5 responds to A-MYB to elaborate the male meiotic program in mice.. *Reproduction (Cambridge, England)*. PMID: 36395073
3. Transcription factor-like 5 is a potential DNA- and RNA-binding protein essential for maintaining male fertility in mice.. *Journal of cell science*. PMID: 34931239
4. Single-nucleus multiomics reveals the gene regulatory networks underlying sex determination of murine primordial germ cells.. *eLife*. PMID: 40063068
5. A-MYB/TCFL5 regulatory architecture ensures the production of pachytene piRNAs in placental mammals.. *RNA (New York, N.Y.)*. PMID: 36241367

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 53.1 |
| 高置信度残基 (pLDDT>90) 占比 | 13.2% |
| 置信残基 (pLDDT 70-90) 占比 | 7.0% |
| 中等置信 (pLDDT 50-70) 占比 | 17.0% |
| 低置信 (pLDDT<50) 占比 | 62.8% |
| 有序区域 (pLDDT>70) 占比 | 20.2% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=53.1），有序残基占 20.2%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011598, IPR036638, IPR039583; Pfam: PF00010 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| PPFIBP2 | 0.574 | 0.000 | — |
| RBM28 | 0.508 | 0.000 | — |
| ALB | 0.487 | 0.000 | — |
| MORN3 | 0.450 | 0.000 | — |
| CHGA | 0.416 | 0.000 | — |
| ZFX | 0.403 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENST00000335351 | psi-mi:"MI:2195"(clash) | pubmed:23622248|imex:IM-30030| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 6，IntAct interactions: 1
- 调控相关比例: 0 / 6 = 0%

**评价**: STRING 6 个预测互作，IntAct 1 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=53.1 + PDB: 无 | pLDDT=53.1, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 6 + 1 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. TCFL5 — Transcription factor-like 5 protein，非常新颖，仅有少数基础研究。
2. 蛋白大小500 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 27 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=53.1），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9UL49
- Protein Atlas: https://www.proteinatlas.org/ENSG00000101190-TCFL5/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TCFL5
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9UL49
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
