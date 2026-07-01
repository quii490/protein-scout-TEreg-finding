---
type: protein-evaluation
gene: "GJD3"
uniprot: "Q8N144"
date: 2026-06-28
tags: [protein-scout, nucleus-cytoplasm, evaluation, rejected]
status: rejected
---

## GJD3 / Gap Junction Delta-3 评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | GJD3 (别名: GJA11, GJC1) |
| 蛋白全称 | Gap junction delta-3 protein / Connexin-31.9 / Cx31.9 |
| UniProt ID | Q8N144 (Swiss-Prot, reviewed) |
| 蛋白大小 | 294 aa |
| UniProt 证据等级 | 1: Evidence at protein level |
| 亚细胞定位 | **Cell membrane; Cell junction, gap junction** (多次跨膜蛋白) |

### 2. 评分总览
| 维度 | 得分 | 权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 0/10 | x4 | 0.0 | 细胞膜间隙连接蛋白; 非核 |
| 蛋白大小 | 5/10 | x1 | 5.0 | 294 aa |
| 新颖性 | 4/10 | x5 | 20.0 | PubMed=38; PPI=459 (间隙连接网络) |
| 三维结构 | 2/10 | x3 | 6.0 | 4次跨膜螺旋; 无高置信 AlphaFold |
| 调控结构域 | 0/10 | x2 | 0.0 | Connexin domain; 无染色质/DNA结合域 |
| PPI | 6/10 | x3 | 18.0 | PPI degree=459 (经BioGRID确认) |
| **加权总分** | | | **49.0/180** | |
| **归一化总分** | | | **27.2/100** | |

### 3. 详细分析

**核定位: 完全不成立 (FAIL)**。GJD3 是一个**间隙连接蛋白** (Connexin family)，定位在细胞膜上，形成跨膜通道 (connexon) 使相邻细胞间进行小分子物质交换。蛋白为 4 次跨膜蛋白 (transmembrane helices at 25-45, 77-97, 137-157, 189-209)，N 端和 C 端均位于胞质侧。**该蛋白不可能进入细胞核**，HPA 标注 "Nucleoplasm; Cell Junctions" 中核质信号是明确的假阳性 (抗体交叉反应或过表达伪影)。

**功能**: 间隙连接通道的核心组件。在血管平滑肌细胞、心脏、结肠、动脉、大脑皮层、肝脏、肺、肾脏、脾脏和睾丸中表达。与 TJP1 (zona occludens protein-1) 相互作用。

**PPI 网络**: PPI degree=459 虽然看起来很可观，但这是在 BioGRID 中经过实验验证的相互作用。这些相互作用主要反映了间隙连接蛋白在膜上的物理复合体形成，而非核内调控网络。高 PPI 数不代表该蛋白参与染色质或转录调控。

**TE 调控潜力**: **零**。间隙连接蛋白的生物学功能是细胞间通讯，与转座元件沉默、染色质重塑或转录调控完全无关。蛋白不含任何 DNA 结合域、组蛋白修饰域或染色质相关模块。

### 4. 总体评价
**27.2/100** | **REJECTED**

**拒绝理由**: GJD3 是一个**细胞膜间隙连接跨膜蛋白**，功能为细胞间通道形成。HPA 标注的核定位为明确假阳性。蛋白不含任何与染色质、转录或 TE 调控相关的结构域。高 PPI 度 (459) 反映的是膜蛋白复合体，而非核调控网络。虽然在筛选数据中因 PPI 高和 hotness=38 获得了 tier=2 的高分，但在生物学本质上完全不符合 TE 调控因子筛选目标。

**关键文献**:
- GJD3/Connexin-31.9 文献主要集中在间隙连接生理学和心血管疾病领域，无 TE 或染色质相关研究。
