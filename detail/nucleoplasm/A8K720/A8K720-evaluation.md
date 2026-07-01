---
type: protein-evaluation
gene: "A8K720"
date: 2026-06-29
tags: [protein-scout, nuclear-protein, evaluation, enriched]
status: shortlisted
---

## A8K720 (cDNA FLJ75040, highly similar to Homo sapiens serum response factor-related protein, RSRFC9) 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 | A8K720 |
| 蛋白全称 | cDNA FLJ75040, highly similar to Homo sapiens serum response factor-related protein, RSRFC9 |
| UniProt ID | A8K720 |
| 蛋白大小 | 495 aa / 54.5 kDa |
| 评估日期 | 2026-06-29 |
| GO-CC 定位 | no known nuclear annotation |

### 2. 评分总览

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 4/10 | ×4 | 16.0 | no known nuclear annotation |
| 蛋白大小 | 9/10 | ×1 | 9.0 | 495 aa |
| 研究新颖性 | 10/10 | ×5 | 50.0 | PubMed=0; TrEMBL entry |
| 三维结构 | 6/10 | ×3 | 18.0 | AF pLDDT available; no experimental PDB |
| 调控结构域 | 8/10 | ×2 | 16.0 | InterPro:IPR022102; InterPro:IPR033896; InterPro:IPR002100; InterPro:IPR036879; Pfam:PF12347; Pfam:PF00319 |
| PPI | 5/10 | ×3 | 15.0 | PPI data limited |
| **加权总分** | | | **124/180** | |
| **归一化总分 (/1.83)** | | | **67.8/100** | 互证: +0 |

### 3. 详细分析

#### 3.1 功能描述

TrEMBL unreviewed entry, function not fully annotated.

#### 3.2 结构域分析

| 来源 | 结构域 ID |
|---|---|
| InterPro | IPR022102 |
| InterPro | IPR033896 |
| InterPro | IPR002100 |
| InterPro | IPR036879 |
| Pfam | PF12347 |
| Pfam | PF00319 |

#### 3.3 核定位

no known nuclear annotation

### 4. 总体评价

**推荐等级**: ⭐⭐ (2/5)

**TE 调控相关性**: 该蛋白缺乏明确的核/染色质定位证据，TE调控潜力极低，不建议作为优先靶标。

### 深度机制分析

A8K720（495 aa, UniProt A8K720）是血清应答因子相关蛋白RSRFC9的同源序列，其结构域包含IPR022102（MEF2样转录因子）、IPR033896（MADS-box/MEF2-type）和IPR002100（MADS-box转录因子，SRF-type/TF），Pfam条目SRF-TF和MADS。MADS-box结构域（约58 aa）是高度保守的DNA结合模块，识别5'-C(A/T)6G-3'（CArG box）基序。RSRFC9属于MEF2（肌细胞增强因子2）家族，该家族成员作为成肌分化和神经发育的关键转录因子，通过MADS域结合富含A/T的DNA序列。

CArG box基序（CCW6GG）与TE之间存在显著关联——CArG box序列在Alu元件中高频出现（尤其在Alu的B box中），并且可能作为MEF2的结合位点激活Alu驱动的报告基因。若A8K720/RSRFC9保留了MADS-box的CArG box结合能力，其可能在Alu元件丰富的基因间区域结合并调控邻近蛋白编码基因的表达。该蛋白的核质定位（加权评分67.8）与MADS-box转录因子的经典核内功能一致。

从TE调控角度，MEF2家族成员已被证明在神经发育过程中通过激活LTR衍生增强子参与TE驱动的基因调控网络。A8K720作为MEF2样蛋白，可能识别和结合散布于基因组中的CArG box基序——包括那些插入到TE衍生调控序列中的CArG box，从而调控这些区域的染色质状态和转录活性。该蛋白的完全未表征状态（PubMed=0）使其成为挖掘MADS-box-TE交叉调控的理想起点。

---

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/A8K720

### 5. 数据来源

- UniProt: https://www.uniprot.org/uniprotkb/A8K720
- AlphaFold: https://alphafold.ebi.ac.uk/entry/A8K720
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=A8K720